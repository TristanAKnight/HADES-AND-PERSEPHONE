# Secrets and Environment Policy

Status: starter policy
Date: 2026-08-19

## Purpose

Protect the continuity shelter from credential leakage while keeping the project reproducible.

This repository may contain source hierarchy, validation code, setup plans, workflow shapes, and public-safe templates. It must not contain private credentials, private account identifiers, raw private exports, session material, or active intimate transcript content.

## Never commit

- `.env` files.
- API keys.
- OAuth tokens or refresh tokens.
- Cookies, session secrets, browser storage, or exported login data.
- Private phone numbers, private email addresses, addresses, IDs, or account recovery details.
- Raw unreviewed archive/JSON bodies.
- Raw screenshots from restricted investigations unless Katerina explicitly approves a redacted version.
- Active scene transcript material.

## Allowed templates

Template files may show variable names without values.

Allowed examples:

```env
LIBRECHAT_ENDPOINT_NAME=
MODEL_API_BASE_URL=
MODEL_API_KEY=replace_me
N8N_WEBHOOK_URL=
OBSIDIAN_VAULT_PATH=
HAP_SNAPSHOT_ROOT=
```

## Local-only files

These files stay on Katerina's machine and out of Git:

- `.env`
- `.env.local`
- `.env.production`
- `secrets.json`
- `tokens.json`
- browser/session dumps
- local model provider keys
- exported private conversations unless redacted and routed

## Required `.gitignore` entries

```gitignore
.env
.env.*
!.env.example
secrets.json
tokens.json
*.pem
*.key
*.p12
*.sqlite
*.db
local_exports/
raw_archive/
quarantine/raw/
snapshots/private/
```

## Redaction rule

A redacted file should preserve structure while removing private values.

Bad:

```json
{"api_key":"sk-live-real-value"}
```

Good:

```json
{"api_key":"[REDACTED_API_KEY]"}
```

## Workflow rule

n8n and local scripts may read secrets from environment variables or local credential stores. Snapshot exports must record that a secret existed only as metadata, never as the secret value.

## Self-check before commit

1. Search for `sk-`, `api_key`, `token`, `secret`, `password`, `Authorization`, `Bearer`, `refresh_token`, and private contact strings.
2. Confirm `.env` is ignored.
3. Confirm raw archive and raw screenshots are absent.
4. Confirm generated outputs are public-safe.
5. Confirm current source hierarchy is preserved.
