#!/usr/bin/env node

// Thin wrapper around shared google-auth module, scoped to 'gmail' service.
// All auth logic (token refresh, rotation handling, persistence) lives in the shared module.

import {
  loadTokenConfig as _loadTokenConfig,
  saveTokenConfig as _saveTokenConfig,
  getDefaultAccount as _getDefaultAccount,
  setDefaultAccount as _setDefaultAccount,
  listAccounts as _listAccounts,
  loadTokens as _loadTokens,
  saveTokens as _saveTokens,
  removeAccount as _removeAccount,
  getAuthClient as _getAuthClient,
  parseAccountArg,
} from '../../../shared/google-auth.js';

const SERVICE = 'gmail';

export function loadTokenConfig() { return _loadTokenConfig(SERVICE); }
export function saveTokenConfig(config) { return _saveTokenConfig(SERVICE, config); }
export function getDefaultAccount() { return _getDefaultAccount(SERVICE); }
export function setDefaultAccount(accountId) { return _setDefaultAccount(SERVICE, accountId); }
export function listAccounts() { return _listAccounts(SERVICE); }
export function loadTokens(accountId = null) { return _loadTokens(SERVICE, accountId); }
export function saveTokens(accountId, tokens, email = null) { return _saveTokens(SERVICE, accountId, tokens, email); }
export function removeAccount(accountId) { return _removeAccount(SERVICE, accountId); }
export function getAuthClient(accountId = null) { return _getAuthClient(SERVICE, accountId); }
export { parseAccountArg };
