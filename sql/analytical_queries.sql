-- Total cases
SELECT COUNT(*) AS total_cases
FROM staging.stg_cases;

-- Cases by request type
SELECT request_type, COUNT(*) AS cases
FROM staging.stg_cases
GROUP BY request_type
ORDER BY cases DESC;

-- Average processing days by request type
SELECT
    request_type,
    ROUND(AVG(processing_days), 2) AS avg_processing_days
FROM staging.stg_cases
WHERE processing_days IS NOT NULL
GROUP BY request_type
ORDER BY avg_processing_days DESC;

-- Status distribution
SELECT status, COUNT(*) AS cases
FROM staging.stg_cases
GROUP BY status
ORDER BY cases DESC;

-- Data quality overview
SELECT
    ROUND(AVG(data_quality_score), 2) AS avg_data_quality_score,
    MIN(data_quality_score) AS min_data_quality_score,
    MAX(data_quality_score) AS max_data_quality_score
FROM staging.stg_cases;

-- Records with low data quality
SELECT
    case_id,
    source_file,
    data_quality_score,
    observations
FROM staging.stg_cases
WHERE data_quality_score < 80
ORDER BY data_quality_score ASC;
