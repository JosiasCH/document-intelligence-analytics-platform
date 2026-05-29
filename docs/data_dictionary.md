# Data Dictionary

| Field | Type | Description |
|---|---|---|
| case_id | string | Unique case identifier. |
| document_type | string | Source document type: PDF, DOCX, TXT. |
| request_type | string | Administrative request category. |
| title | string | Case title or subject. |
| applicant_name | string | Main applicant. Public data uses anonymized names. |
| coauthors | string | Coauthors separated by commas. |
| advisor | string | Advisor or reviewer. |
| faculty | string | Faculty or organizational unit. |
| program | string | Academic program or department. |
| submission_date | date | Date when the case was submitted. |
| review_date | date | Date when the case was reviewed. |
| decision_date | date | Date when the final decision was issued. |
| status | string | Current status. |
| result | string | Final result or decision. |
| observations | string | Main observation or issue. |
| processing_days | integer | Days between submission date and decision date. |
| data_quality_score | float | Percentage of mandatory fields completed and valid. |
| source_file | string | File name processed by the pipeline. |
| extraction_timestamp | timestamp | Timestamp when the extraction was executed. |
