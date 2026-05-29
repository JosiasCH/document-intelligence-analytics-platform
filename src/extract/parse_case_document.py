from __future__ import annotations

from datetime import datetime
from typing import Optional

import pandas as pd


FIELD_LABELS = {
    "case id": "case_id",
    "document type": "document_type",
    "request type": "request_type",
    "title": "title",
    "applicant": "applicant_name",
    "coauthors": "coauthors",
    "advisor": "advisor",
    "faculty": "faculty",
    "program": "program",
    "submission date": "submission_date",
    "review date": "review_date",
    "decision date": "decision_date",
    "status": "status",
    "result": "result",
    "observations": "observations",
}

DATE_FIELDS = ["submission_date", "review_date", "decision_date"]

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


def _empty_record() -> dict:
    return {field: None for field in FIELD_LABELS.values()}


def _normalize_label(label: str) -> str:
    return label.strip().lower()


def _parse_key_value_lines(text: str) -> dict:
    """
    Parses documents line by line to avoid multiline regex errors.

    Example:
        Program:
        Submission Date: 2025-05-19

    The previous regex-based parser could incorrectly capture
    'Submission Date: 2025-05-19' as the program value. This line-based
    parser prevents that issue.
    """
    record = _empty_record()

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line or ":" not in line:
            continue

        label, value = line.split(":", 1)
        normalized_label = _normalize_label(label)

        if normalized_label not in FIELD_LABELS:
            continue

        field_name = FIELD_LABELS[normalized_label]
        clean_value = value.strip()

        record[field_name] = clean_value if clean_value else None

    return record


def _parse_date(value: Optional[str]) -> Optional[str]:
    if not value:
        return None

    parsed = pd.to_datetime(value, errors="coerce", dayfirst=False)

    if pd.isna(parsed):
        return None

    return parsed.date().isoformat()


def _calculate_processing_days(
    submission_date: Optional[str],
    decision_date: Optional[str],
) -> Optional[int]:
    if not submission_date or not decision_date:
        return None

    try:
        start = datetime.fromisoformat(submission_date).date()
        end = datetime.fromisoformat(decision_date).date()
    except ValueError:
        return None

    return (end - start).days


def _calculate_data_quality_score(record: dict) -> float:
    valid_count = sum(1 for field in MANDATORY_FIELDS if record.get(field))
    return round((valid_count / len(MANDATORY_FIELDS)) * 100, 2)


def parse_case_document(text: str, source_file: str | None = None) -> dict:
    record = _parse_key_value_lines(text)

    for field in DATE_FIELDS:
        record[field] = _parse_date(record.get(field))

    record["processing_days"] = _calculate_processing_days(
        record.get("submission_date"),
        record.get("decision_date"),
    )

    record["data_quality_score"] = _calculate_data_quality_score(record)
    record["source_file"] = source_file

    return record