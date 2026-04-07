#!/usr/bin/env node

import { google } from 'googleapis';
import { readFileSync } from 'fs';
import minimist from 'minimist';
import { getAuthClient, parseAccountArg } from './auth/auth-utils.js';
import { logAction } from './action-logger.js';

function markdownToHtml(md) {
  let html = md;

  // Headers (h1-h4)
  html = html.replace(/^#### (.+)$/gm, '<h4 style="margin:16px 0 8px 0;font-size:14px;color:#333;">$1</h4>');
  html = html.replace(/^### (.+)$/gm, '<h3 style="margin:18px 0 8px 0;font-size:16px;color:#333;">$1</h3>');
  html = html.replace(/^## (.+)$/gm, '<h2 style="margin:20px 0 10px 0;font-size:18px;color:#222;">$1</h2>');
  html = html.replace(/^# (.+)$/gm, '<h1 style="margin:24px 0 12px 0;font-size:22px;color:#111;">$1</h1>');

  // Bold and italic
  html = html.replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>');
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');

  // Horizontal rules
  html = html.replace(/^---+$/gm, '<hr style="border:none;border-top:1px solid #ddd;margin:16px 0;">');

  // Unordered lists: collect consecutive lines starting with - or *
  html = html.replace(/((?:^[ ]*[-*] .+\n?)+)/gm, (match) => {
    const items = match.trim().split('\n').map(line => {
      const text = line.replace(/^[ ]*[-*] /, '');
      return `  <li style="margin:4px 0;">${text}</li>`;
    }).join('\n');
    return `<ul style="margin:8px 0;padding-left:24px;">\n${items}\n</ul>`;
  });

  // Ordered lists: collect consecutive lines starting with 1. 2. etc
  html = html.replace(/((?:^[ ]*\d+\. .+\n?)+)/gm, (match) => {
    const items = match.trim().split('\n').map(line => {
      const text = line.replace(/^[ ]*\d+\. /, '');
      return `  <li style="margin:4px 0;">${text}</li>`;
    }).join('\n');
    return `<ol style="margin:8px 0;padding-left:24px;">\n${items}\n</ol>`;
  });

  // Paragraphs: wrap remaining text blocks (lines not already wrapped in HTML tags)
  // Split by double newlines for paragraph breaks
  const blocks = html.split(/\n{2,}/);
  html = blocks.map(block => {
    block = block.trim();
    if (!block) return '';
    // Skip blocks that already start with HTML tags
    if (/^<(h[1-4]|ul|ol|hr|li|p|div|table|blockquote)/i.test(block)) return block;
    // Convert single newlines within a paragraph to <br>
    block = block.replace(/\n/g, '<br>\n');
    return `<p style="margin:8px 0;line-height:1.5;">${block}</p>`;
  }).join('\n');

  // Wrap in a styled container
  return `<div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;font-size:14px;color:#333;max-width:680px;">\n${html}\n</div>`;
}

function createEmailMessage(to, subject, body, options = {}) {
  const { cc, bcc, html, replyTo } = options;

  const headers = [
    `To: ${to}`,
    `Subject: ${subject}`,
  ];

  if (cc) headers.push(`Cc: ${cc}`);
  if (bcc) headers.push(`Bcc: ${bcc}`);
  if (replyTo) headers.push(`Reply-To: ${replyTo}`);

  headers.push('Content-Type: text/html; charset=utf-8');
  headers.push('MIME-Version: 1.0');

  // If --html is provided, use it directly. Otherwise, convert --body from markdown to HTML.
  const htmlBody = html || markdownToHtml(body);
  // MIME requires a blank line (double CRLF) between headers and body
  const message = headers.join('\r\n') + '\r\n\r\n' + htmlBody;

  return Buffer.from(message)
    .toString('base64')
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=+$/, '');
}

async function sendEmail(args) {
  // Support --body-file to read body from a file (for long content)
  if (args['body-file'] && !args.body) {
    args.body = readFileSync(args['body-file'], 'utf-8');
  }

  // Validate required args
  if (!args.to || !args.subject || !args.body) {
    throw new Error('Missing required arguments: --to, --subject, and --body (or --body-file) are required');
  }

  // Get authenticated client for specified account (or default)
  const accountId = parseAccountArg(args);
  const oauth2Client = await getAuthClient(accountId);

  const gmail = google.gmail({ version: 'v1', auth: oauth2Client });

  // Create email
  const encodedMessage = createEmailMessage(
    args.to,
    args.subject,
    args.body,
    {
      cc: args.cc,
      bcc: args.bcc,
      html: args.html,
      replyTo: args['reply-to']
    }
  );

  // Send email
  const result = await gmail.users.messages.send({
    userId: 'me',
    requestBody: {
      raw: encodedMessage
    }
  });

  return {
    success: true,
    messageId: result.data.id,
    threadId: result.data.threadId,
    to: args.to,
    subject: args.subject,
    account: accountId || 'default'
  };
}

// Main execution
const args = minimist(process.argv.slice(2));
const startTime = Date.now();

sendEmail(args)
  .then(result => {
    // Log the action
    logAction('send', args, result, {
      account: result.account,
      duration: Date.now() - startTime
    });

    console.log(JSON.stringify(result, null, 2));
  })
  .catch(error => {
    const errorResult = {
      success: false,
      error: error.message
    };

    // Log the failed action
    logAction('send', args, errorResult, {
      account: args.account || 'default',
      duration: Date.now() - startTime,
      failed: true
    });

    console.error(JSON.stringify(errorResult, null, 2));
    process.exit(1);
  });
