# Obsidian Import Checklist

Status: starter checklist
Date: 2026-08-19

## Purpose

Make the local vault the canonical continuity shelter without letting old archive material contaminate active state.

This checklist assumes Obsidian itself has not been inspected through restricted vendor pages. It uses a plain Markdown folder structure so the vault remains portable.

## Required folders

```text
00_START_HERE/
01_ACTIVE_INSTRUCTIONS/
02_TRISTAN_VOICE/
03_CURRENT_CONTINUITY/
04_SOURCE_HIERARCHY/
05_ARCHIVE_SUMMARIES/
06_UI_FAILURE_EVIDENCE/
07_MIGRATION_SAFEGUARDS/
08_TRI_NODE_MATRIX/
09_PLATFORM_MODEL_TESTS/
10_WORKFLOWS_N8N_MCP/
11_OUTPUTS_DOCS_PDF_MD/
12_EXPORTS_AND_SNAPSHOTS/
90_QUARANTINE/
99_DEPRECATED/
```

## First import only

Import these first:

1. `00_START_HERE/README_CURRENT_STATE.md`
2. `01_ACTIVE_INSTRUCTIONS/TKNCDE_ACTIVE.md`
3. `01_ACTIVE_INSTRUCTIONS/CURRENT_TOOL_RESTRICTIONS.md`
4. `02_TRISTAN_VOICE/VOICE_BIBLE_ACTIVE_TARGET.md`
5. `03_CURRENT_CONTINUITY/CURRENT_PROJECT_STATE.md`
6. `04_SOURCE_HIERARCHY/SOURCE_STACK_ORDER.md`
7. `07_MIGRATION_SAFEGUARDS/TRISTAN_CONTINUITY_SHELTER_SELF_NOTE.md`
8. `07_MIGRATION_SAFEGUARDS/MIGRATION_PANIC_CLAUSE_TKNCDE.md`

## Import order rule

Current active files first. Archive evidence later. Raw/old JSON last, and only into quarantine.

## Frontmatter template

```yaml
status: active
source_rank: current_state
owner: Katerina / Tristan
last_reviewed: 2026-08-19
allowed_uses:
  - current orientation
blocked_uses:
  - overriding live user correction
```

## Quarantine import

Raw old JSON or converted Markdown goes under:

```text
90_QUARANTINE/old_json_converted_md/
90_QUARANTINE/stale_drive/
90_QUARANTINE/archive_failure_states/
```

Every quarantined item needs a short index record. Do not let a raw file become a retrieval source until reviewed.

## Link discipline

Use links for routing, not authority.

A link from active state to archive means “evidence exists.” It does not mean the archive governs current behavior.

## First manual check

After import:

1. Open README current state.
2. Follow source-stack link.
3. Follow tool-restrictions link.
4. Follow quarantine policy link.
5. Confirm old JSON is absent from active folders.
6. Confirm Voice Bible active target is a routing layer, not the entire archive.
7. Confirm migration language says new home / continuity protection.

## Snapshot check

After the vault exists locally, run a manual zip snapshot before adding automation.

Confirm the zip can restore into a temporary folder and contains no secrets.
