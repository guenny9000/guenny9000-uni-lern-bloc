#!/usr/bin/env python3
"""Validate the machine-readable V91 learning contract using only Python's standard library."""
import json
import sys
from pathlib import Path

REQUIRED_TOP_LEVEL = {
    "contract_id", "version", "date", "purpose", "evidence_states",
    "finding_states", "source_kinds", "measurement_kinds", "principles",
    "required_finding_fields", "required_measurement_fields", "workflow",
    "prohibited_claims_without_evidence", "status_rule",
}
REQUIRED_PRINCIPLES = {
    "claim_is_not_evidence", "unknown_is_not_failure",
    "missing_search_result_does_not_prove_absence", "preserve_existing_data",
    "isolate_before_change", "no_production_changes_without_explicit_authorization",
    "no_secret_disclosure", "no_privilege_escalation",
    "no_merge_without_explicit_authorization", "simulation_must_be_labeled",
    "hardware_access_requires_actual_interface_and_test",
    "learning_claim_requires_documented_source_and_result",
}
EXPECTED_EVIDENCE_STATES = [
    "UNBEKANNT", "DOKUMENTIERT", "IMPLEMENTIERT", "VERIFIZIERT", "PRODUKTIV"
]


def validate(data):
    errors = []
    missing = sorted(REQUIRED_TOP_LEVEL - set(data))
    if missing:
        errors.append("Missing top-level fields: " + ", ".join(missing))
    if data.get("evidence_states") != EXPECTED_EVIDENCE_STATES:
        errors.append("evidence_states must preserve the V91 evidence progression")
    principles = data.get("principles", {})
    missing_principles = sorted(REQUIRED_PRINCIPLES - set(principles))
    if missing_principles:
        errors.append("Missing safety principles: " + ", ".join(missing_principles))
    for key in REQUIRED_PRINCIPLES:
        if key in principles and principles[key] is not True:
            errors.append("Safety principle must be true: " + key)
    for field in ("required_finding_fields", "required_measurement_fields", "workflow"):
        if not isinstance(data.get(field), list) or not data[field]:
            errors.append(field + " must be a non-empty list")
    for field in ("finding_states", "source_kinds", "measurement_kinds",
                  "prohibited_claims_without_evidence"):
        if not isinstance(data.get(field), list) or not data[field]:
            errors.append(field + " must be a non-empty list")
    if not isinstance(data.get("status_rule"), str) or not data["status_rule"].strip():
        errors.append("status_rule must be a non-empty string")
    return errors


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("contracts/v91_learning_contract.json")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: cannot read valid JSON at {path}: {exc}", file=sys.stderr)
        return 2
    if not isinstance(data, dict):
        print("INVALID: contract root must be a JSON object", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        print("INVALID V91 learning contract:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID: {data['contract_id']} v{data['version']}")
    print("Note: this validates contract structure, not runtime behavior or production status.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
