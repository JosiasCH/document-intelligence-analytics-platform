from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path
from typing import Optional

import pandas as pd

FIELD_PATTERNS = {
    "case_id": r"Case ID:\s*(.+)",
    "document_type": r"Document Type:\s*(.+)",
    "request_type": r"Request Type:\s*(.+)",
    "title": r"Title:\s*(.+)",
    "applicant_name": r"Applicant:\s*(.+)",
    "coauthors": r"Coauthors:\s*(.+)",
    "advisor": r"Advisor:\s*(.+)",
    "faculty": r"Faculty:\s*(.+)",
    "program": r"Program:\s*(.+)",
    "submission_date": r"Submission Date:\s*(.+)",
    "review_date": r"Review Date:\s*(.+)",
    "decision_date": r"Decision Date:\s*(.+)",
    "status": r"Status:\s*(.+)",
    "result": r"Result:\s*(.+)",
    "observations": r"Observations:\s*(.+)",
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


def _extract_field(text: str, pattern: str) -> Optional[str]:
    match = re.search(pattern, text, flags=re.IGNORECASE)
    if not match:
        return None
    value = match.group(1).strip()
    return value if value else None


def _parse_date(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    parsed = pd.to_datetime(value, errors="coerce", dayfirst=False)
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def _calculate_processing_days(submission_date: Optional[str], decision_date: Optional[str]) -> Optional[int]:
    if not submission_date or not decision_date:
        return None
    start = datetime.fromisoformat(submission_date).date()
    end = datetime.fromisoformat(decision_date).date()
    return (end - start).days


def _calculate_data_quality_score(record: dict) -> float:
    valid_count = sum(1 for field in MANDATORY_FIELDS if record.get(field))
    return round((valid_count / len(MANDATORY_FIELDS)) * 100, 2)


def parse_case_document(text: str, source_file: str | None = None) -> dict:
    record = {
        field: _extract_field(text, pattern)
        for field, pattern in FIELD_PATTERNS.items()
    }

    for field in DATE_FIELDS:
        record[field] = _parse_date(record.get(field))

    record["processing_days"] = _calculate_processing_days(
        record.get("submission_date"),
        record.get("decision_date"),
    )
    record["data_quality_score"] = _calculate_data_quality_score(record)
    record["source_file"] = source_file

    return record
