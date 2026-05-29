from __future__ import annotations

MANDATORY_FIELDS = [
    "case_id",
    "request_type",
    "title",
    "applicant_name",
    "faculty",
    "program",
    "submission_date",
    "decision_date",
    "status",
    "result",
]


def validate_record(record: dict) -> list[dict]:
    issues = []

    for field in MANDATORY_FIELDS:
        if not record.get(field):
            issues.append({
                "case_id": record.get("case_id"),
                "source_file": record.get("source_file"),
                "issue_type": "missing_mandatory_field",
                "issue_description": f"Missing mandatory field: {field}",
            })

    processing_days = record.get("processing_days")
    if processing_days is not None and processing_days < 0:
        issues.append({
            "case_id": record.get("case_id"),
            "source_file": record.get("source_file"),
            "issue_type": "invalid_date_sequence",
            "issue_description": "decision_date occurs before submission_date",
        })

    return issues
