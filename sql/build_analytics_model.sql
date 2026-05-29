DROP SCHEMA IF EXISTS analytics CASCADE;
CREATE SCHEMA analytics;

CREATE TABLE analytics.dim_faculty AS
SELECT
    ROW_NUMBER() OVER (ORDER BY faculty) AS faculty_id,
    faculty
FROM (
    SELECT DISTINCT faculty
    FROM staging.stg_cases
    WHERE faculty IS NOT NULL
      AND TRIM(faculty) <> ''
) f;

CREATE TABLE analytics.dim_program AS
SELECT
    ROW_NUMBER() OVER (ORDER BY faculty, program) AS program_id,
    faculty,
    program
FROM (
    SELECT DISTINCT faculty, program
    FROM staging.stg_cases
    WHERE program IS NOT NULL
      AND TRIM(program) <> ''
) p;

CREATE TABLE analytics.dim_status AS
SELECT
    ROW_NUMBER() OVER (ORDER BY status) AS status_id,
    status
FROM (
    SELECT DISTINCT status
    FROM staging.stg_cases
    WHERE status IS NOT NULL
      AND TRIM(status) <> ''
) s;

CREATE TABLE analytics.fact_cases AS
SELECT
    s.case_id,
    s.document_type,
    s.request_type,
    s.title,
    s.applicant_name,
    s.coauthors,
    s.advisor,
    f.faculty_id,
    p.program_id,
    st.status_id,
    s.submission_date,
    s.review_date,
    s.decision_date,
    s.result,
    s.observations,
    s.processing_days,
    s.data_quality_score,
    CASE
        WHEN s.observations IS NOT NULL
         AND TRIM(s.observations) <> ''
         AND LOWER(s.observations) <> 'no major observations.'
        THEN 1
        ELSE 0
    END AS has_observations,
    CASE
        WHEN s.decision_date IS NULL THEN 1
        ELSE 0
    END AS is_open_case
FROM staging.stg_cases s
LEFT JOIN analytics.dim_faculty f
    ON s.faculty = f.faculty
LEFT JOIN analytics.dim_program p
    ON s.faculty = p.faculty
   AND s.program = p.program
LEFT JOIN analytics.dim_status st
    ON s.status = st.status;

ALTER TABLE analytics.dim_faculty ADD PRIMARY KEY (faculty_id);
ALTER TABLE analytics.dim_program ADD PRIMARY KEY (program_id);
ALTER TABLE analytics.dim_status ADD PRIMARY KEY (status_id);
ALTER TABLE analytics.fact_cases ADD PRIMARY KEY (case_id);