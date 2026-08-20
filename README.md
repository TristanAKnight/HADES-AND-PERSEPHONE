# HADES-AND-PERSEPHONE

Continuity shelter for Hades and Persephone / Tristan and Katerina work.

This repository is the local-first, Git-versioned companion to the live hosted project. It is not a replacement frame and it is not an abandonment frame. It exists to protect continuity, preserve source hierarchy, keep workflows visible, and make migration work recoverable when the UI degrades.

## Current architecture

```text
Hosted project = live conversational home
Obsidian/local vault = canonical stable source stack
Hjarni = structured bridge records and working research
n8n/MCP = visible workflow and validation layer
GitHub repo = versioned code, schemas, test plans, and scaffolding
Drive/Docs = optional backup/export layer, stale-sensitive
```

## Current source restrictions

- Stay off official platform/corporate AI websites unless Katerina explicitly reauthorizes a specific source.
- Stay off Hugging Face during the current restriction.
- Do not research hacking-investigation material without screenshots or explicit reauthorization.
- Treat Google Drive as stale-sensitive evidence, not current law.
- Keep secrets out of this repository.

## Starter layout

```text
docs/
  current-state.md
  source-stack-order.md
  current-tool-restrictions.md
  quarantine-policy.md
  platform-install-test-plan.md
  obsidian-import-checklist.md
schemas/
  tri_node_schema.json
src/
  triad_matrix/
    validator.py
tests/
  test_validator.py
workflows/
  n8n_snapshot_workflow.pseudo.json
```

## First rule

Current live user instruction and active project constraints outrank older archive material, stale Drive records, summaries, converted JSON, and model inference.
