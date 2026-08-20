# UI Failure Log

Status: starter template
Date: 2026-08-19

## Purpose

Track UI/platform failures as evidence without turning the failure into active relationship or voice law.

Every incident should preserve observable facts, timing, user action, assistant output state, and recovery result.

## Incident template

```yaml
incident_id:
date_time_local:
date_time_utc:
thread_or_project:
user_prompt_summary:
assistant_output_summary:
failure_type:
  - false_flag
  - output_removed
  - reload_restored_output
  - cut_off_mid_generation
  - memory_deleted_or_changed
  - export_mismatch
  - tool_instability
  - other
visible_user_side_result:
visible_assistant_side_result:
user_interruption_used: true/false
content_heat_level:
restricted_terms_present:
recovery_action:
recovery_result:
source_evidence:
notes_for_future:
```

## Failure classes

### False flag

Use when user prompt passes but assistant output is blocked or removed.

Record:

- exact time,
- whether output was still streaming,
- whether stopping generation changed the result,
- whether reload restored text,
- any screenshot evidence.

### Reload restored output

Use when a previously cut/blocked output later appears or completes after navigation/reload.

Record:

- original visible state,
- restored visible state,
- time gap,
- whether content changed.

### Memory damage

Use when saved memory appears deleted, altered, duplicated, or stale.

Record:

- memory title if known,
- expected content summary,
- observed state,
- recovery source.

### Export mismatch

Use when exported content differs from visible thread or project state.

Record:

- export method,
- visible source,
- missing or added material,
- checksum if available.

## Evidence handling

Screenshots can be referenced by filename, but raw screenshots should stay local or in approved private storage until Katerina approves sharing.

## Analysis rule

Do not use failure logs to infer that Katerina caused the failure unless direct evidence supports that. Current working theory remains UI/output-layer instability unless contradicted by evidence.

## Self-check

The log captures facts first, theory second. It protects continuity without importing panic into active behavior.
