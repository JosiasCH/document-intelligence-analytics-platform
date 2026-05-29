from src.extract.parse_case_document import parse_case_document


def test_parse_case_document_complete_record():
    text = """
    Case ID: CASE-2025-001
    Document Type: Synthetic DOCX
    Request Type: APC
    Title: Automation of Administrative Review Processes
    Applicant: Applicant_001
    Coauthors: Applicant_002, Applicant_003
    Advisor: Advisor_001
    Faculty: Engineering
    Program: Industrial Engineering
    Submission Date: 2025-03-01
    Review Date: 2025-03-10
    Decision Date: 2025-03-15
    Status: Approved
    Result: Approved without observations
    Observations: Complete documentation
    """

    record = parse_case_document(text, source_file="sample.docx")

    assert record["case_id"] == "CASE-2025-001"
    assert record["request_type"] == "APC"
    assert record["processing_days"] == 14
    assert record["data_quality_score"] == 100.0
