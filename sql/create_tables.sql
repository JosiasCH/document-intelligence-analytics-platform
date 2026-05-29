CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS analytics;

DROP TABLE IF EXISTS raw.raw_documents CASCADE;
CREATE TABLE raw.raw_documents (
    raw_document_id SERIAL PRIMARY KEY,
    source_file TEXT NOT NULL,
    document_type TEXT,
    raw_text TEXT,
    extraction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS staging.stg_cases CASCADE;
CREATE TABLE staging.stg_cases (
    case_id TEXT PRIMARY KEY,
    document_type TEXT,
    request_type TEXT,
    title TEXT,
    applicant_name TEXT,
    coauthors TEXT,
    advisor TEXT,
    faculty TEXT,
    program TEXT,
    submission_date DATE,
    review_date DATE,
    decision_date DATE,
    status TEXT,
    result TEXT,
    observations TEXT,
    processing_days INTEGER,
    data_quality_score NUMERIC(5,2),
    source_file TEXT,
    extraction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS analytics.dim_faculty CASCADE;
CREATE TABLE analytics.dim_faculty AS
SELECT DISTINCT
    ROW_NUMBER() OVER (ORDER BY faculty) AS faculty_key,
    faculty
FROM staging.stg_cases
WHERE faculty IS NOT NULL;

DROP TABLE IF EXISTS analytics.dim_program CASCADE;
CREATE TABLE analytics.dim_program AS
SELECT DISTINCT
    ROW_NUMBER() OVER (ORDER BY program) AS program_key,
    program
FROM staging.stg_cases
WHERE program IS NOT NULL;

DROP TABLE IF EXISTS analytics.dim_status CASCADE;
CREATE TABLE analytics.dim_status AS
SELECT DISTINCT
    ROW_NUMBER() OVER (ORDER BY status) AS status_key,
    status
FROM staging.stg_cases
WHERE status IS NOT NULL;

DROP TABLE IF EXISTS analytics.fact_cases CASCADE;
CREATE TABLE analytics.fact_cases AS
SELECT
    case_id,
    document_type,
    request_type,
    title,
    faculty,
    program,
    status,
    result,
    submission_date,
    review_date,
    decision_date,
    processing_days,
    data_quality_score,
    source_file,
    extraction_timestamp
FROM staging.stg_cases;

DROP TABLE IF EXISTS staging.data_quality_log CASCADE;
CREATE TABLE staging.data_quality_log (
    quality_log_id SERIAL PRIMARY KEY,
    case_id TEXT,
    source_file TEXT,
    issue_type TEXT,
    issue_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
