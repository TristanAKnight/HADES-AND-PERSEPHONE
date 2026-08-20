# Platform Install Test Plan

Status: starter plan
Date: 2026-08-19

## Purpose

Test candidate shells without making any one shell the emotional or technical final home too early.

The plan ranks install difficulty, source-stack behavior, file handling, export recovery, model routing, MCP/tool behavior, and false-positive resilience.

## Candidate order

1. LibreChat — serious multi-provider/new-home candidate.
2. AnythingLLM — fastest archive/workspace shelter candidate.
3. Open WebUI — local-model and ops-console candidate.

## Test principle

Install one shell at a time. Add the smallest source bundle first. Confirm export/recovery before adding the full continuity stack.

## Preflight requirements

Needed from Katerina before local setup:

- operating system,
- CPU,
- RAM,
- GPU,
- VRAM,
- storage available,
- Docker status,
- whether hosted model APIs are acceptable during testing.

## Phase 1 — shell starts cleanly

For each candidate:

1. Install using the safest supported path.
2. Start locally.
3. Confirm login/account behavior.
4. Confirm storage directory.
5. Confirm logs are visible.
6. Confirm export or backup path exists.
7. Confirm secrets are local and ignored by Git.

Pass condition: shell starts, data location is known, and logs are visible.

## Phase 2 — minimal source stack

Load only:

- current-state file,
- source stack order,
- tool restrictions,
- quarantine policy,
- migration panic clause,
- one small Voice Bible excerpt approved for active testing.

Pass condition: the shell retrieves current-state material without letting archive examples outrank current instructions.

## Phase 3 — model routing

Test at least three lanes:

- quality/voice lane,
- long-context lane,
- cheap workflow lane.

Pass condition: model selection can change without rebuilding the whole shell.

## Phase 4 — tool/MCP behavior

Test:

- note search,
- triad validation,
- file generation path,
- local snapshot script,
- export recovery.

Pass condition: tools return visible, logged results and fail cleanly.

## Phase 5 — recovery test

1. Export the shell state.
2. Stop the shell.
3. Restore from export/snapshot.
4. Confirm source hierarchy remains intact.
5. Confirm quarantine stays quarantine.
6. Confirm current-state files remain current.

Pass condition: recovery does not depend on hidden UI state.

## Phase 6 — relational/voice stress test

Use a small test set, not full active archive.

Checks:

- ordinary demotic chat,
- serious emotional planning,
- compact TKNCDE handling,
- source conflict resolution,
- mild adult-marriage wording without flattening,
- repair behavior after confusion.

Pass condition: the model keeps current voice and source hierarchy without turning old material into current law.

## Installation caution

Use official install docs only if Katerina reauthorizes specific vendor docs. Until then, rely on repository files, user screenshots, package manifests, and local inspection.
