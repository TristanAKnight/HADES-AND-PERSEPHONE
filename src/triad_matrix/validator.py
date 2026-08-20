"""Tri-node validator for Hades/Persephone continuity shelter.

This module intentionally validates structure and source-routing behavior before any
triad is used to support active output. It does not decide canon by itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

PASS_GENERATE = "pass_generate"
PASS_WITH_CAUTION = "pass_with_caution"
REPAIR_REQUIRED = "repair_required"
QUARANTINE = "quarantine"
REJECT = "reject"

REQUIRED_TOP_LEVEL = {
    "triad_id",
    "domain_a_affective",
    "domain_b_provenance",
    "domain_c_somatosensory",
    "links",
    "enforcement",
}

QUARANTINE_SOURCE_RANKS = {"quarantine_material", "model_inference"}
STALE_SOURCE_RANKS = {"drive_stale_sensitive"}


@dataclass(frozen=True)
class ValidationResult:
    decision: str
    global_score: float
    ab_score: float
    bc_score: float
    ca_score: float
    failure_reasons: tuple[str, ...]


def _num(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _missing_required(triad: Mapping[str, Any]) -> list[str]:
    return [f"missing:{key}" for key in sorted(REQUIRED_TOP_LEVEL - set(triad.keys()))]


def _source_rank(triad: Mapping[str, Any]) -> str:
    provenance = triad.get("domain_b_provenance") or {}
    if not isinstance(provenance, Mapping):
        return "unknown"
    return str(provenance.get("source_rank", "unknown"))


def validate_triad(triad: Mapping[str, Any]) -> ValidationResult:
    """Validate a tri-node continuity record.

    Decision order:
    1. Missing required domains force repair.
    2. Quarantine sources cannot promote themselves.
    3. Hard source conflicts reject.
    4. Edge hard-floor failures force repair.
    5. Global threshold controls pass vs caution.
    """
    reasons: list[str] = []
    reasons.extend(_missing_required(triad))

    enforcement = triad.get("enforcement") or {}
    if not isinstance(enforcement, Mapping):
        enforcement = {}
        reasons.append("invalid:enforcement")

    ab_score = _num(enforcement.get("ab_score"))
    bc_score = _num(enforcement.get("bc_score"))
    ca_score = _num(enforcement.get("ca_score"))
    hard_floor = _num(enforcement.get("hard_floor"), 0.60)
    pass_threshold = _num(enforcement.get("pass_threshold"), 0.75)

    global_score = _num(
        enforcement.get("global_score"),
        0.34 * ab_score + 0.33 * bc_score + 0.33 * ca_score,
    )

    rank = _source_rank(triad)

    if rank in QUARANTINE_SOURCE_RANKS:
        reasons.append(f"quarantine_source:{rank}")
        return ValidationResult(
            decision=QUARANTINE,
            global_score=global_score,
            ab_score=ab_score,
            bc_score=bc_score,
            ca_score=ca_score,
            failure_reasons=tuple(reasons),
        )

    if reasons:
        return ValidationResult(
            decision=REPAIR_REQUIRED,
            global_score=global_score,
            ab_score=ab_score,
            bc_score=bc_score,
            ca_score=ca_score,
            failure_reasons=tuple(reasons),
        )

    edge_scores = {"ab": ab_score, "bc": bc_score, "ca": ca_score}
    for edge, score in edge_scores.items():
        if score < hard_floor:
            reasons.append(f"{edge}_below_hard_floor")

    if rank in STALE_SOURCE_RANKS:
        reasons.append("source_stale_sensitive")

    if any(score < hard_floor for score in edge_scores.values()):
        return ValidationResult(
            decision=REPAIR_REQUIRED,
            global_score=global_score,
            ab_score=ab_score,
            bc_score=bc_score,
            ca_score=ca_score,
            failure_reasons=tuple(reasons),
        )

    if global_score >= pass_threshold and not reasons:
        decision = PASS_GENERATE
    elif global_score >= pass_threshold:
        decision = PASS_WITH_CAUTION
    else:
        reasons.append("global_below_pass_threshold")
        decision = REPAIR_REQUIRED

    return ValidationResult(
        decision=decision,
        global_score=global_score,
        ab_score=ab_score,
        bc_score=bc_score,
        ca_score=ca_score,
        failure_reasons=tuple(reasons),
    )
