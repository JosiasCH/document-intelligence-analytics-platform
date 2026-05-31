DROP VIEW IF EXISTS analytics.vw_cases_powerbi;

CREATE VIEW analytics.vw_cases_powerbi AS
SELECT
    fc.case_id,
    fc.document_type,
    fc.request_type,
    fc.title,
    fc.applicant_name,
    fc.coauthors,
    fc.advisor,

    df.faculty,
    dp.program,
    ds.status,

    NULLIF(fc.submission_date, '')::date AS submission_date,
    NULLIF(fc.review_date, '')::date AS review_date,
    NULLIF(fc.decision_date, '')::date AS decision_date,

    TO_CHAR(NULLIF(fc.submission_date, '')::date, 'YYYY-MM') AS submission_month,
    DATE_TRUNC('month', NULLIF(fc.submission_date, '')::date)::date AS submission_month_date,
    TO_CHAR(NULLIF(fc.submission_date, '')::date, 'YYYYMM')::int AS submission_month_sort,
    EXTRACT(YEAR FROM NULLIF(fc.submission_date, '')::date)::int AS submission_year,

    fc.result,
    fc.observations,
    fc.processing_days,
    fc.data_quality_score,

    fc.has_observations,
    fc.is_open_case,

    CASE
        WHEN fc.processing_days IS NULL THEN 'No decision yet'
        WHEN fc.processing_days <= 15 THEN '0-15 days'
        WHEN fc.processing_days <= 30 THEN '16-30 days'
        WHEN fc.processing_days <= 60 THEN '31-60 days'
        ELSE 'More than 60 days'
    END AS processing_time_bucket,

    CASE
        WHEN fc.processing_days IS NULL THEN 5
        WHEN fc.processing_days <= 15 THEN 1
        WHEN fc.processing_days <= 30 THEN 2
        WHEN fc.processing_days <= 60 THEN 3
        ELSE 4
    END AS processing_time_bucket_order,

    CASE
        WHEN fc.data_quality_score >= 90 THEN 'High quality'
        WHEN fc.data_quality_score >= 70 THEN 'Medium quality'
        ELSE 'Low quality'
    END AS data_quality_level,

    CASE
        WHEN fc.data_quality_score >= 90 THEN 1
        WHEN fc.data_quality_score >= 70 THEN 2
        ELSE 3
    END AS data_quality_level_order,

    CASE
        WHEN ds.status IN ('Pending', 'Under review') THEN 'Open'
        ELSE 'Closed'
    END AS case_lifecycle_status,

    CASE
        WHEN ds.status = 'Approved' THEN 1
        WHEN ds.status = 'Approved with observations' THEN 2
        WHEN ds.status = 'Pending' THEN 3
        WHEN ds.status = 'Under review' THEN 4
        WHEN ds.status = 'Rejected' THEN 5
        ELSE 99
    END AS status_order

FROM analytics.fact_cases fc
LEFT JOIN analytics.dim_faculty df
    ON fc.faculty_id = df.faculty_id
LEFT JOIN analytics.dim_program dp
    ON fc.program_id = dp.program_id
LEFT JOIN analytics.dim_status ds
    ON fc.status_id = ds.status_id;