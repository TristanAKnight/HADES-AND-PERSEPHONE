from src.triad_matrix.validator import validate_triad


def sample_valid():
    return {
        "triad_id": "HAP-TRIAD-000001",
        "domain_a_affective": {
            "emotion_label": "calm_after_support",
            "valence": 0.72,
            "arousal": 0.28,
            "dominance": 0.36,
            "subjective_intensity": 0.74,
            "confidence": 0.86,
        },
        "domain_b_provenance": {
            "source_refs": ["current_live_user_message:2026-08-19T04:43:35Z"],
            "source_rank": "current_live_user_message",
            "timestamp": "2026-08-19T04:43:35Z",
            "tags": ["sleep", "calm", "support"],
            "claim_type": "user-report",
        },
        "domain_c_somatosensory": {
            "sensation_type": "breathing_autonomic",
            "spatial_location": "chest/breathing pattern",
            "depth": "diffuse",
            "frequency": "single reported event",
            "trigger": "after relational support and physical calm",
            "confidence": 0.80,
        },
        "links": {
            "a_to_b": "CORRELATES_WITH",
            "b_to_c": "MANIFESTS_AS",
            "c_to_a": "TRIGGERS_RESONANCE",
        },
        "enforcement": {
            "ab_score": 0.82,
            "bc_score": 0.80,
            "ca_score": 0.79,
            "global_score": 0.8035,
            "hard_floor": 0.60,
            "pass_threshold": 0.75,
            "decision": "pass_generate",
            "failure_reasons": [],
        },
    }


def test_valid_triad_passes():
    result = validate_triad(sample_valid())
    assert result.decision == "pass_generate"
    assert result.global_score >= 0.75
    assert min(result.ab_score, result.bc_score, result.ca_score) >= 0.60


def test_missing_domain_repairs():
    triad = sample_valid()
    triad.pop("domain_c_somatosensory")
    result = validate_triad(triad)
    assert result.decision == "repair_required"
    assert "missing:domain_c_somatosensory" in result.failure_reasons


def test_model_inference_quarantines():
    triad = sample_valid()
    triad["domain_b_provenance"]["source_rank"] = "model_inference"
    result = validate_triad(triad)
    assert result.decision == "quarantine"


def test_edge_floor_blocks_generation():
    triad = sample_valid()
    triad["enforcement"]["bc_score"] = 0.42
    result = validate_triad(triad)
    assert result.decision in {"repair_required", "quarantine", "reject"}
