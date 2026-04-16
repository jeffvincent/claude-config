#!/usr/bin/env node

import { google } from 'googleapis';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join } from 'path';
import { homedir } from 'os';

const SECRETS_BASE = join(homedir(), '.claude', 'secrets');

function tokenPath(service) {
  return join(SECRETS_BASE, service, 'tokens.json');
}

function credentialsPath(service) {
  return join(SECRETS_BASE, service, 'credentials.json');
}

export function loadTokenConfig(service) {
  const path = tokenPath(service);
  if (!existsSync(path)) {
    throw new Error(`Token file not found for ${service}. Run: npm run setup`);
  }

  const data = JSON.parse(readFileSync(path, 'utf8'));

  // Auto-migrate old single-account format
  if (data.access_token && !data.accounts) {
    const migratedConfig = {
      defaultAccount: 'default',
      accounts: { default: data }
    };
    saveTokenConfig(service, migratedConfig);
    return migratedConfig;
  }

  return data;
}

export function saveTokenConfig(service, config) {
  writeFileSync(tokenPath(service), JSON.stringify(config, null, 2), { mode: 0o600 });
}

export function getDefaultAccount(service) {
  const config = loadTokenConfig(service);
  return config.defaultAccount || Object.keys(config.accounts)[0];
}

export function setDefaultAccount(service, accountId) {
  const config = loadTokenConfig(service);
  if (!config.accounts[accountId]) {
    throw new Error(`Account '${accountId}' not found`);
  }
  config.defaultAccount = accountId;
  saveTokenConfig(service, config);
}

export function listAccounts(service) {
  const config = loadTokenConfig(service);
  return Object.entries(config.accounts).map(([id, data]) => ({
    id,
    email: data.email || 'unknown',
    scope: data.scope || '',
    isDefault: id === config.defaultAccount
  }));
}

export function loadTokens(service, accountId = null) {
  const config = loadTokenConfig(service);
  const targetAccount = accountId || config.defaultAccount;

  if (!config.accounts[targetAccount]) {
    const available = Object.keys(config.accounts).join(', ');
    throw new Error(
      `Account '${targetAccount}' not found. Available accounts: ${available}`
    );
  }

  return config.accounts[targetAccount];
}

export function saveTokens(service, accountId, tokens, email = null) {
  const path = tokenPath(service);
  const config = existsSync(path) ? loadTokenConfig(service) : { accounts: {} };

  if (!config.accounts) {
    config.accounts = {};
  }

  const existingEmail = config.accounts[accountId]?.email;

  config.accounts[accountId] = {
    ...tokens,
    ...(email && { email }),
    ...(!email && existingEmail && { email: existingEmail })
  };

  if (!config.defaultAccount || Object.keys(config.accounts).length === 1) {
    config.defaultAccount = accountId;
  }

  saveTokenConfig(service, config);
}

export function removeAccount(service, accountId) {
  const config = loadTokenConfig(service);

  if (!config.accounts[accountId]) {
    throw new Error(`Account '${accountId}' not found`);
  }

  delete config.accounts[accountId];

  if (config.defaultAccount === accountId) {
    const remaining = Object.keys(config.accounts);
    config.defaultAccount = remaining.length > 0 ? remaining[0] : null;
  }

  saveTokenConfig(service, config);
}

function loadCredentials(service) {
  const path = credentialsPath(service);
  if (!existsSync(path)) {
    throw new Error(`Credentials file not found at ${path}`);
  }
  return JSON.parse(readFileSync(path, 'utf8'));
}

/**
 * Get authenticated OAuth2 client with automatic token refresh and rotation handling.
 *
 * Key behaviors:
 * - Proactively refreshes expired/expiring tokens before returning the client
 * - Explicitly saves refreshed credentials to disk (not just via event handler)
 * - Re-reads tokens from disk in the event handler to avoid stale-closure overwrites
 * - Handles missing expiry_date by forcing a refresh to validate the token
 */
export async function getAuthClient(service, accountId = null) {
  const tokens = loadTokens(service, accountId);
  const credentials = loadCredentials(service);
  const { client_id, client_secret } = credentials.installed || credentials.web;

  const oauth2Client = new google.auth.OAuth2(client_id, client_secret);
  oauth2Client.setCredentials(tokens);

  const targetAccount = accountId || getDefaultAccount(service);

  // Listen for token refresh events — captures rotated refresh tokens during API calls.
  // Re-reads from disk to avoid overwriting tokens saved by a concurrent process.
  oauth2Client.on('tokens', (newTokens) => {
    let currentTokens;
    try {
      currentTokens = loadTokens(service, targetAccount);
    } catch {
      currentTokens = tokens;
    }
    const merged = {
      ...currentTokens,
      ...newTokens,
      // Preserve existing refresh_token if Google doesn't issue a new one
      refresh_token: newTokens.refresh_token || currentTokens.refresh_token,
    };
    saveTokens(service, targetAccount, merged);
  });

  // Proactively refresh if:
  // - expiry_date is missing (can't verify token validity without trying)
  // - access token is expired or expiring within 5 minutes
  const now = Date.now();
  const fiveMinutes = 5 * 60 * 1000;
  const needsRefresh = !tokens.expiry_date || (tokens.expiry_date - now) < fiveMinutes;

  if (needsRefresh) {
    if (!tokens.refresh_token) {
      throw new Error(
        `No refresh_token found for ${service} account '${targetAccount}'. ` +
        `Run: npm run setup`
      );
    }

    try {
      await oauth2Client.getAccessToken();
    } catch (err) {
      throw new Error(
        `Token refresh failed for ${service} account '${targetAccount}': ${err.message}\n` +
        `This usually means the refresh token has been revoked or expired.\n` +
        `Re-authenticate with: npm run setup`
      );
    }

    // Explicitly save the refreshed credentials — don't rely solely on the event handler.
    // oauth2Client.credentials contains the full updated token set after refresh.
    const refreshedCreds = oauth2Client.credentials;
    const merged = {
      ...tokens,
      ...refreshedCreds,
      refresh_token: refreshedCreds.refresh_token || tokens.refresh_token,
    };
    saveTokens(service, targetAccount, merged);
  }

  return oauth2Client;
}

export function parseAccountArg(args) {
  return args.account || null;
}
