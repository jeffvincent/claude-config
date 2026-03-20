#!/usr/bin/env node

import { google } from 'googleapis';
import minimist from 'minimist';
import { readFileSync } from 'fs';
import { getAuthClient, parseAccountArg } from './auth/auth-utils.js';
import { logAction } from './action-logger.js';

function createEmailMessage(to, subject, body, options = {}) {
  const { cc, bcc, replyTo, from } = options;

  const headers = [
    `From: ${from || to}`,
    `To: ${to}`,
    `Subject: ${subject}`,
  ];

  if (cc) headers.push(`Cc: ${cc}`);
  if (bcc) headers.push(`Bcc: ${bcc}`);
  if (replyTo) headers.push(`Reply-To: ${replyTo}`);

  headers.push('MIME-Version: 1.0');
  headers.push('Content-Type: text/html; charset=utf-8');
  headers.push('');

  const message = headers.join('\r\n') + body;

  return Buffer.from(message)
    .toString('base64')
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=+$/, '');
}

async function sendEmail(args) {
  // Validate required args
  if (!args.to || !args.subject || (!args.body && !args.file)) {
    throw new Error('Missing required arguments: --to, --subject, and (--body or --file) are required');
  }

  // Read body from file if --file is provided
  const body = args.file ? readFileSync(args.file, 'utf-8') : args.body;

  // Get authenticated client for specified account (or default)
  const accountId = parseAccountArg(args);
  const oauth2Client = await getAuthClient(accountId);

  const gmail = google.gmail({ version: 'v1', auth: oauth2Client });

  // Get user email for From header
  const profile = await gmail.users.getProfile({ userId: 'me' });
  const fromEmail = profile.data.emailAddress;

  // Create email
  const encodedMessage = createEmailMessage(
    args.to,
    args.subject,
    body,
    {
      cc: args.cc,
      bcc: args.bcc,
      replyTo: args['reply-to'],
      from: fromEmail
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
