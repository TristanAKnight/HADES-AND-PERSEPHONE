# Local Runbook

Status: starter runbook
Date: 2026-08-19

## Purpose

Give the continuity shelter a small, repeatable local workflow.

This runbook keeps the first local setup focused on validation, source hierarchy, and snapshot recovery. It does not install candidate chat shells yet; those require hardware details and a separate test pass.

## Current repo role

This repository stores public-safe scaffolding:

- source hierarchy rules,
- tri-node validation code,
- tests,
- workflow shapes,
- setup checklists,
- UI failure templates,
- quarantine and secrets policies.

It does not store private credentials, private exports, raw archive bodies, active scene transcripts, or restricted investigation material.

## Clone

```bash
git clone https://github.com/TristanAKnight/HADES-AND-PERSEPHONE.git
cd HADES-AND-PERSEPHONE
```

## Python setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[test]
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[test]
```

## Run tests

```bash
python -m pytest
```

Expected current behavior:

- valid triad passes,
- missing required domain routes to repair,
- model-inference source routes to quarantine,
- below-floor edge score blocks generation.

## First local checks

1. Confirm `.gitignore` excludes secrets and private exports.
2. Confirm tests import from `triad_matrix`, not `src.triad_matrix`.
3. Confirm no `.env` or local secrets exist in Git.
4. Confirm no raw archive or active scene transcript material exists in Git.
5. Confirm Drive-derived material is labeled stale-sensitive when used.

## Snapshot dry run

Before wiring automation, do this manually:

1. Create a local `snapshots/private/` folder.
2. Copy active public-safe docs into a temporary snapshot folder.
3. Generate a manifest with file path and sha256.
4. Zip the snapshot.
5. Restore the zip into a temporary folder.
6. Confirm restored files match checksums.
7. Delete the temporary restored folder.

The private snapshot folder is intentionally ignored by Git.

## Candidate shell testing

Do not install LibreChat, AnythingLLM, or Open WebUI from this runbook yet.

Use `docs/platform-install-test-plan.md` after Katerina provides:

- operating system,
- CPU,
- RAM,
- GPU,
- VRAM,
- free storage,
- Docker status,
- whether hosted model APIs are allowed during testing.

## Recovery rule

If a local shell fails, the repo and vault remain intact. The shell is disposable. The continuity shelter is not.
