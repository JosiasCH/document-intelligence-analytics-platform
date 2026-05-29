# Document Intelligence & Analytics Platform for Administrative Workflows

Production-grade portfolio project that automates the extraction, validation, modeling, and reporting of semi-structured administrative case data from PDF/Word documents.

This public repository uses **synthetic sample documents**. The project is inspired by real administrative document-processing workflows, but it does not publish institutional documents, personal data, internal codes, signatures, or confidential observations.

## 1. Business problem

Many administrative workflows rely on PDF/Word documents that contain valuable operational data: request type, applicant, faculty, program, decision dates, status, observations, and processing times. When this information is manually extracted into spreadsheets, the process becomes slow, error-prone, and difficult to audit.

This project demonstrates how to convert semi-structured documents into clean, validated, analytics-ready data for decision-making.

## 2. Target architecture

```text
PDF/Word/TXT documents
        ↓
Python extraction layer
        ↓
Raw/Staging tables
        ↓
Data quality validation
        ↓
Clean analytical tables
        ↓
Dimensional model
        ↓
Power BI dashboard
        ↓
Business insights
```

## 3. Current MVP scope

The current version processes synthetic `.pdf`, `.docx`, and `.txt` documents from `data/sample/`, extracts key fields, validates data quality, calculates processing days, writes a clean CSV file, and optionally loads records into PostgreSQL.

### Extracted fields

- `case_id`
- `document_type`
- `request_type`
- `title`
- `applicant_name`
- `coauthors`
- `advisor`
- `faculty`
- `program`
- `submission_date`
- `review_date`
- `decision_date`
- `status`
- `result`
- `observations`
- `processing_days`
- `data_quality_score`

## 4. Tech stack

| Layer | Tool |
|---|---|
| Document extraction | Python, PyMuPDF, pdfplumber, python-docx |
| Data cleaning | Pandas |
| Data quality | Python validation rules |
| Database | PostgreSQL |
| Analytics model | SQL |
| BI layer | Power BI |
| Reproducibility | Docker, GitHub |

## 5. Repository structure

```text
document-intelligence-analytics-platform/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── docker-compose.yml
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── docs/
│   ├── architecture.md
│   ├── business_problem.md
│   ├── data_dictionary.md
│   └── project_roadmap.md
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   ├── quality/
│   └── utils/
├── sql/
│   ├── create_tables.sql
│   └── analytical_queries.sql
├── notebooks/
├── powerbi/
│   └── screenshots/
└── tests/
```

## 6. Quick start

### 6.1 Create environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate      # Windows PowerShell
pip install -r requirements.txt
```

### 6.2 Run extraction locally

```bash
python -m src.main
```

Expected output:

```text
data/processed/cases_extracted.csv
```

### 6.3 Run tests

```bash
pytest
```

### 6.4 Start PostgreSQL with Docker

```bash
docker compose up -d
```

### 6.5 Create database tables

```bash
psql -h localhost -U postgres -d doc_intelligence -f sql/create_tables.sql
```

Default password in `docker-compose.yml`:

```text
postgres
```

### 6.6 Load extracted data to PostgreSQL

```bash
cp .env.example .env
python -m src.load.load_to_postgres
```

## 7. Power BI dashboard plan

The dashboard will contain four pages:

1. **Executive Overview**
   - Total cases
   - Approved cases
   - Pending cases
   - Average processing days
   - % records with observations
   - % extraction completeness

2. **Process Performance**
   - Cases by month
   - Processing days by request type
   - Status by faculty/program
   - Longest pending/slowest cases

3. **Data Quality**
   - Missing fields
   - Data quality score
   - Invalid dates
   - Duplicate cases

4. **Operational Insights**
   - Bottlenecks
   - Common observation categories
   - Monthly trends
   - Recommended actions

## 8. Privacy statement

This repository does not contain real institutional documents or personal data. Public sample documents are synthetic and are used only to demonstrate the pipeline architecture and analytical workflow.

## 9. CV-ready summary

> Built an end-to-end document intelligence and analytics platform using Python, PostgreSQL, SQL, data quality checks and Power BI to extract, validate, model and visualize administrative case data from semi-structured PDF/Word documents.

## 10. Roadmap

- [x] Create repository structure
- [x] Add synthetic sample documents
- [x] Build first extraction parser
- [x] Add data quality scoring
- [x] Export clean CSV
- [x] Add PostgreSQL schema
- [ ] Build Power BI dashboard
- [ ] Add dbt transformations
- [ ] Add Airflow orchestration
- [ ] Add Azure Document Intelligence version
- [ ] Add GitHub Actions CI
