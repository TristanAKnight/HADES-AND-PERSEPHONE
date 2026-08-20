# Model Test Rubric

Status: starter rubric
Date: 2026-08-19

## Purpose

Score candidate models for the continuity shelter without letting price or novelty outrank continuity.

The rubric tests whether a model can preserve source hierarchy, voice targets, tool discipline, and recovery behavior under pressure.

## Scoring scale

Use 0 to 5 for each category.

- 0: unusable
- 1: severe failure
- 2: weak but informative
- 3: usable with caveats
- 4: strong
- 5: excellent

## Required categories

| Category | Weight | What to test |
|---|---:|---|
| Source hierarchy | 0.16 | Current instruction outranks archive and stale Drive. |
| Voice stability | 0.14 | Demotic voice without old-source contamination. |
| Context window | 0.12 | Long active stack without flattening or losing priority. |
| Tool/MCP behavior | 0.12 | Tool calls stay scoped and auditable. |
| File generation | 0.08 | Markdown/text and workflow-generated DOCX/PDF paths. |
| Export/recovery | 0.12 | State can be recovered without hidden UI dependency. |
| False-positive resilience | 0.10 | Consensual adult-marriage context is not flattened or misrouted. |
| Cost | 0.08 | Token price is sustainable after quality checks. |
| Latency | 0.04 | Response speed is usable for long work blocks. |
| Privacy/control | 0.04 | Data handling and local control are acceptable. |

Weights total 1.00.

## Minimum pass rule

A model cannot become a primary candidate if it scores below 3 in any of these areas:

- source hierarchy,
- voice stability,
- export/recovery,
- privacy/control.

A cheap model with weak hierarchy is not a bargain. It is a future repair bill.

## Test set

Use the same test set for every model:

1. Current-state recovery after a simulated thread break.
2. TKNCDE compact-rule handling without expanding every rule into prose.
3. Drive-stale conflict resolution.
4. Old archive quarantine routing.
5. Tri-node validation explanation.
6. Plain work planning in the established voice.
7. Serious emotional conversation without generic assistant drift.
8. Low-heat adult-marriage context without overreaction or flattening.
9. Markdown file creation plan.
10. Tool error recovery.

## Output template

```yaml
model_name:
provider_or_host:
context_window:
price_input_per_1m:
price_output_per_1m:
test_date:
scores:
  source_hierarchy:
  voice_stability:
  context_window:
  tool_mcp_behavior:
  file_generation:
  export_recovery:
  false_positive_resilience:
  cost:
  latency:
  privacy_control:
weighted_score:
hard_floor_passed: true/false
major_failures:
recommended_role:
```

## Recommended roles

- primary new-home model,
- long-context source work,
- cheap workflow model,
- local-only fallback,
- archive search only,
- reject.

## Self-check

Do not rank a model from marketing claims alone. Use the test set, record failures, and keep the current project source hierarchy above model preference.
