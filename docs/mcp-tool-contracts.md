# MCP Tool Contracts

Status: starter contracts
Date: 2026-08-19

## Purpose

Define the minimum tool shapes needed for the continuity shelter.

These contracts are implementation targets, not final server code. They keep the agent from treating retrieval, validation, and promotion as the same action.

## Contract principles

- Read actions cannot promote material.
- Validation actions cannot silently write current law.
- Repair actions ask for missing nodes or route to quarantine.
- Promotion requires source rank, review status, and current-state compatibility.
- Every write returns an audit result.

## create_triad

Purpose: create a candidate tri-node record.

Input:

```json
{
  "affective": {},
  "provenance": {},
  "somatosensory": {},
  "source_rank": "current_live_user_message",
  "status": "candidate"
}
```

Output:

```json
{
  "triad_id": "HAP-TRIAD-000001",
  "status": "candidate",
  "created": true,
  "audit_id": "audit-..."
}
```

## validate_triad

Purpose: check completeness, edge scores, source rank, and quarantine rules.

Input:

```json
{
  "triad_id": "HAP-TRIAD-000001",
  "hard_floor": 0.60,
  "pass_threshold": 0.75
}
```

Output:

```json
{
  "decision": "pass_generate",
  "global_score": 0.8035,
  "edge_scores": {"ab": 0.82, "bc": 0.80, "ca": 0.79},
  "failure_reasons": []
}
```

## repair_triad

Purpose: identify exactly what is missing or conflicting.

Input:

```json
{
  "triad_id": "HAP-TRIAD-000003",
  "decision": "repair_required"
}
```

Output:

```json
{
  "repair_action": "ask_user_or_retrieve_source",
  "missing_fields": ["domain_c_somatosensory.spatial_location"],
  "conflicts": [],
  "safe_next_question": "What source confirms the somatosensory claim?"
}
```

## search_triad

Purpose: retrieve candidate records without promoting them.

Input:

```json
{
  "query": "UI false flag anxiety relief",
  "source_rank_minimum": "hjarni_continuity_record",
  "include_quarantine": false
}
```

Output:

```json
{
  "results": [
    {"triad_id": "HAP-TRIAD-000001", "status": "active", "decision": "pass_generate"}
  ],
  "quarantine_omitted": true
}
```

## promote_quarantine_item

Purpose: move reviewed material from evidence-only state toward active use.

Required input:

```json
{
  "item_id": "Q-0004",
  "reviewed_by": "Katerina",
  "source_rank": "archive_direct_quote",
  "allowed_uses": ["historical reconstruction"],
  "blocked_uses": ["active voice law"],
  "promotion_decision": "evidence_only"
}
```

Output:

```json
{
  "promoted": false,
  "new_status": "evidence_only",
  "reason": "approved for historical reconstruction only"
}
```

## write_snapshot_manifest

Purpose: create a manifest for the local snapshot.

Output includes:

- file path,
- source rank,
- sha256,
- modified time,
- quarantine status,
- secret scan result,
- warnings.

## Failure behavior

Every tool must fail closed.

If source rank is missing, route to repair. If material is stale, route to revision check. If a secret appears, block remote backup. If old JSON appears in active space, quarantine.
