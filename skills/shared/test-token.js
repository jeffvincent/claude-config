#!/usr/bin/env node

/**
 * Diagnostic script to test OAuth token health for Google services.
 *
 * Usage:
 *   node test-token.js --service google-calendar
 *   node test-token.js --service gmail
 *   node test-token.js --service gmail --account work
 *   node test-token.js --service google-calendar --refresh   # force a refresh and save
 */

import minimist from 'minimist';
import {
  loadTokens,
  loadTokenConfig,
  getDefaultAccount,
  getAuthClient,
} from './google-auth.js';

const args = minimist(process.argv.slice(2));
const service = args.service || args.s;
const accountId = args.account || args.a || null;
const forceRefresh = args.refresh || args.r || false;

if (!service) {
  console.error('Usage: node test-token.js --service <google-calendar|gmail> [--account <id>] [--refresh]');
  process.exit(1);
}

async function diagnose() {
  console.log(`\n--- Token Diagnostics for "${service}" ---\n`);

  // Step 1: Check token file exists and load config
  let config, tokens, targetAccount;
  try {
    config = loadTokenConfig(service);
    targetAccount = accountId || getDefaultAccount(service);
    tokens = loadTokens(service, targetAccount);
    console.log(`Account:        ${targetAccount}`);
    console.log(`Email:          ${tokens.email || '(not stored)'}`);
    console.log(`Accounts:       ${Object.keys(config.accounts).join(', ')}`);
  } catch (err) {
    console.error(`FAIL: Cannot load tokens — ${err.message}`);
    process.exit(1);
  }

  // Step 2: Check token fields
  console.log(`\nToken fields present:`);
  console.log(`  access_token:  ${tokens.access_token ? 'YES (' + tokens.access_token.slice(0, 20) + '...)' : 'MISSING'}`);
  console.log(`  refresh_token: ${tokens.refresh_token ? 'YES (' + tokens.refresh_token.slice(0, 20) + '...)' : 'MISSING'}`);
  console.log(`  expiry_date:   ${tokens.expiry_date ? new Date(tokens.expiry_date).toISOString() : 'MISSING'}`);
  console.log(`  token_type:    ${tokens.token_type || 'MISSING'}`);
  console.log(`  scope:         ${tokens.scope || 'MISSING'}`);

  if (!tokens.refresh_token) {
    console.error(`\nCRITICAL: No refresh_token stored. This means tokens cannot be renewed.`);
    console.error(`Re-run: npm run setup (in the ${service} skill directory)`);
    process.exit(1);
  }

  // Step 3: Check expiry
  if (tokens.expiry_date) {
    const now = Date.now();
    const remaining = tokens.expiry_date - now;
    const mins = Math.round(remaining / 60000);
    if (remaining > 0) {
      console.log(`\nAccess token expires in ${mins} minutes.`);
    } else {
      console.log(`\nAccess token EXPIRED ${Math.abs(mins)} minutes ago.`);
    }
  } else {
    console.log(`\nWARNING: No expiry_date stored — cannot tell if access token is valid.`);
  }

  // Step 4: Attempt refresh
  console.log(`\n--- Testing token refresh ---\n`);
  try {
    const client = await getAuthClient(service, targetAccount);
    const creds = client.credentials;
    console.log(`SUCCESS: Token refresh worked.`);
    console.log(`  New expiry: ${creds.expiry_date ? new Date(creds.expiry_date).toISOString() : '(not set)'}`);
    console.log(`  refresh_token preserved: ${creds.refresh_token ? 'YES' : 'NO'}`);

    // Verify saved tokens match
    const savedTokens = loadTokens(service, targetAccount);
    if (savedTokens.expiry_date === creds.expiry_date) {
      console.log(`  Tokens persisted to disk: YES`);
    } else {
      console.warn(`  WARNING: Tokens may not have been saved correctly to disk.`);
      console.warn(`    In-memory expiry:  ${creds.expiry_date}`);
      console.warn(`    On-disk expiry:    ${savedTokens.expiry_date}`);
    }
  } catch (err) {
    console.error(`FAIL: Token refresh failed — ${err.message}`);
    console.error(`\nThis usually means:`);
    console.error(`  1. The refresh token was revoked (re-run npm run setup)`);
    console.error(`  2. The Google Cloud project OAuth consent screen is in "Testing" mode`);
    console.error(`     (tokens expire after 7 days in testing mode)`);
    console.error(`  3. The OAuth client credentials were regenerated`);
    process.exit(1);
  }

  console.log(`\n--- All checks passed ---\n`);
}

diagnose().catch(err => {
  console.error(`Unexpected error: ${err.message}`);
  process.exit(1);
});
