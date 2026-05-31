<h1 align="center">
  Document Intelligence & Analytics Platform for Administrative Workflows
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
  <br/>
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/PyMuPDF-PDF%20Extraction-2B6CB0?style=for-the-badge" />
  <img src="https://img.shields.io/badge/python--docx-Word%20Extraction-6B7280?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Pytest-Tested-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" />
</p>

<p align="center">
  An end-to-end analytics engineering project that converts semi-structured administrative documents into validated, modeled, and decision-ready data for operational reporting.
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#problem-statement">Problem Statement</a> ·
  <a href="#solution">Solution</a> ·
  <a href="#dashboard">Dashboard</a> ·
  <a href="#how-to-run-locally">Run Locally</a> ·
  <a href="#data-privacy">Data Privacy</a>
</p>

---

## Overview

Administrative teams often manage case-based workflows through semi-structured documents such as application forms, review memos, committee reports, and decision letters. These documents contain valuable operational information, but the data is difficult to analyze when it is not stored in a structured database.

This project addresses that problem by creating a reproducible pipeline that turns document-based case information into structured analytical data.

```text
PDF / Word / TXT documents
        ↓
Python extraction layer
        ↓
Data quality validation
        ↓
Processed CSV output
        ↓
PostgreSQL staging tables
        ↓
Analytics dimensional model
        ↓
Power BI-ready SQL view
        ↓
Power BI dashboard
```

The public version uses synthetic documents to preserve privacy while maintaining the structure and analytical complexity of a realistic administrative workflow.

---

## Problem Statement

Document-based administrative workflows can make operational reporting slow and inconsistent. When case information is distributed across files and spreadsheets, teams often face the following issues:

- case tracking depends on manual updates;
- missing fields are difficult to identify systematically;
- processing delays are not visible in real time;
- reporting requires repeated spreadsheet preparation;
- operational bottlenecks are hard to detect;
- decision-makers do not have a consolidated view of workflow performance.

The objective is to automate the extraction, validation, modeling, and visualization of administrative case data so that workflow performance can be monitored through reliable metrics.

---

## Solution

The platform extracts structured information from semi-structured documents and converts it into a clean analytical model.

The current version includes:

- synthetic administrative documents in `.txt`, `.docx`, and `.pdf` formats;
- Python-based document extraction;
- field parsing and date normalization;
- data quality scoring;
- missing-field detection;
- PostgreSQL database running in Docker;
- staging and analytics schemas;
- dimensional model with fact and dimension tables;
- Power BI-ready SQL view;
- Power BI dashboard with four analytical pages;
- reusable Power BI design system with a warm executive visual style.

---

## Technologies Used

| Area | Tools |
|---|---|
| Document extraction | Python, PyMuPDF, python-docx |
| Data processing | Pandas |
| Database | PostgreSQL |
| Infrastructure | Docker, Docker Compose |
| Data modeling | SQL, dimensional modeling |
| Data quality | Python validation rules, SQL checks |
| Reporting | Power BI Desktop |
| Testing | Pytest |
| Version control | Git, GitHub |
| Visual design | Power BI JSON theme, custom 2000 × 2000 canvas backgrounds |

---

## Repository Structure

```text
document-intelligence-analytics-platform/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── docker-compose.yml
│
├── data/
│   ├── raw/
│   ├── sample/
│   └── processed/
│
├── docs/
│   ├── architecture.md
│   ├── business_problem.md
│   ├── data_dictionary.md
│   └── project_roadmap.md
│
├── scripts/
│   └── generate_sample_documents.py
│
├── src/
│   ├── extract/
│   ├── load/
│   ├── quality/
│   └── utils/
│
├── sql/
│   ├── create_tables.sql
│   ├── build_analytics_model.sql
│   ├── create_powerbi_view.sql
│   └── analytical_queries.sql
│
├── tests/
│   └── test_parser.py
│
├── powerbi/
│   ├── document_intelligence_dashboard.pbix
│   ├── screenshots/
│   │   ├── executive_overview.png
│   │   ├── data_quality_monitoring.png
│   │   ├── process_performance.png
│   │   └── operational_insights.png
│   └── design/
│
└── notebooks/
```

---

## Data Pipeline

### 1. Synthetic Document Generation

The project includes a script that generates synthetic administrative case documents. The documents preserve the structure of a case-based review process without exposing real names, internal records, institutional documents, or confidential observations.

The generated documents include variations such as:

- approved cases;
- rejected cases;
- pending cases;
- cases under review;
- cases with missing program fields;
- cases with missing advisor fields;
- cases with invalid processing dates;
- cases with observations.

### 2. Document Extraction

The extraction layer reads documents from the sample folder and extracts key-value fields such as:

- case ID;
- document type;
- request type;
- title;
- applicant;
- coauthors;
- advisor;
- faculty;
- program;
- submission date;
- review date;
- decision date;
- status;
- result;
- observations.

The parser works line by line to avoid common extraction errors, such as capturing the next field when a value is missing.

### 3. Data Quality Validation

The pipeline calculates a data quality score for each record and identifies issues related to completeness and consistency.

Current validation rules include:

- required field completeness;
- missing program detection;
- missing advisor detection;
- invalid processing time detection;
- open cases without decision dates;
- parsing issues caused by empty fields;
- suspicious values in categorical fields.

### 4. PostgreSQL Load

Processed records are loaded into PostgreSQL using a staging schema.

Main staging table:

```text
staging.stg_cases
```

The database runs locally through Docker using port `5433`.

### 5. Analytics Model

The analytics layer converts staging data into a reporting model.

Main analytics objects:

```text
analytics.dim_faculty
analytics.dim_program
analytics.dim_status
analytics.fact_cases
analytics.vw_cases_powerbi
```

The Power BI view includes additional reporting fields such as:

- submission month;
- month sort key;
- processing time bucket;
- processing time bucket order;
- data quality level;
- data quality level order;
- case lifecycle status;
- status order.

---

## Data Model

The current analytics model follows a simple star-schema structure.

```text
analytics.dim_faculty
        ↓
analytics.fact_cases
        ↑
analytics.dim_program
        ↑
analytics.dim_status
```

### Fact Table

`analytics.fact_cases` stores one row per administrative case.

Main measures and attributes include:

- case ID;
- request type;
- applicant;
- advisor;
- faculty key;
- program key;
- status key;
- submission date;
- review date;
- decision date;
- processing days;
- data quality score;
- observation flag;
- open case flag.

### Dimensions

| Dimension | Purpose |
|---|---|
| `dim_faculty` | Groups cases by faculty |
| `dim_program` | Groups cases by academic or administrative program |
| `dim_status` | Standardizes review status categories |

### Power BI View

`analytics.vw_cases_powerbi` joins fact and dimension tables into a reporting-ready view. This keeps Power BI simpler and keeps business logic close to the database layer.

---

## Dashboard

The Power BI dashboard includes four pages:

1. **Executive Overview**  
   High-level KPIs for case volume, approval status, open cases, processing time, observations, and data quality.

2. **Data Quality Monitoring**  
   Monitoring page for extraction completeness, missing fields, records requiring review, and data quality indicators.

3. **Process Performance**  
   Operational performance page focused on case volume, processing time, request types, and workflow status by faculty.

4. **Operational Insights**  
   Decision-oriented page highlighting bottlenecks, long-processing cases, observed cases, rejected cases, and review priorities.

### Executive Overview

![Executive Overview](powerbi/screenshots/executive_overview.png)

### Data Quality Monitoring

![Data Quality Monitoring](powerbi/screenshots/data_quality_monitoring.png)

### Process Performance

![Process Performance](powerbi/screenshots/process_performance.png)

### Operational Insights

![Operational Insights](powerbi/screenshots/operational_insights.png)

---

## Key Metrics

| Metric | Description |
|---|---|
| Total Cases | Number of processed administrative cases |
| Approved Cases | Cases approved with or without observations |
| Open Cases | Cases still pending or under review |
| Closed Cases | Cases with a final review outcome |
| Average Processing Days | Average time between submission and decision |
| Long Processing Cases | Cases taking more than 30 days |
| Observation Rate | Share of cases with observations |
| Data Quality Score | Average completeness score across extracted records |
| Records Requiring Review | Records flagged by quality rules |
| Missing Program Field | Records without a program value |
| Missing Advisor Field | Records without an advisor value |
| Invalid Processing Time | Records with negative processing duration |
| Open Cases Without Decision | Open cases without decision dates |

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/JosiasCH/document-intelligence-analytics-platform.git
cd document-intelligence-analytics-platform
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate synthetic documents

```bash
python scripts/generate_sample_documents.py
```

### 5. Run the extraction pipeline

```bash
python -m src.main
```

Expected output:

```text
Processed documents: 30
Clean output: data/processed/cases_extracted.csv
Quality issues output: data/processed/data_quality_issues.csv
```

### 6. Start PostgreSQL with Docker

```bash
docker compose up -d
```

The PostgreSQL container is exposed locally through port `5433`.

Connection details:

```text
Host: 127.0.0.1
Port: 5433
Database: doc_intelligence
User: postgres
Password: postgres
```

### 7. Create database tables

```powershell
Get-Content .\sql\create_tables.sql | docker exec -i doc_intelligence_postgres psql -U postgres -d doc_intelligence
```

### 8. Load processed data into PostgreSQL

Create the local environment file:

```powershell
copy .env.example .env
```

Then load the data:

```bash
python -m src.load.load_to_postgres
```

Expected output:

```text
Loaded 30 records into staging.stg_cases
```

### 9. Build the analytics model

```powershell
Get-Content .\sql\build_analytics_model.sql | docker exec -i doc_intelligence_postgres psql -U postgres -d doc_intelligence
```

### 10. Create the Power BI reporting view

```powershell
Get-Content .\sql\create_powerbi_view.sql | docker exec -i doc_intelligence_postgres psql -U postgres -d doc_intelligence
```

### 11. Validate the reporting view

```powershell
docker exec -it doc_intelligence_postgres psql -U postgres -d doc_intelligence -c "SELECT COUNT(*) FROM analytics.vw_cases_powerbi;"
```

Expected result:

```text
count
-----
30
```

---

## Power BI Connection

To connect Power BI Desktop to PostgreSQL:

```text
Get data → PostgreSQL database
```

Use:

```text
Server: 127.0.0.1:5433
Database: doc_intelligence
Data Connectivity mode: Import
```

Credentials:

```text
Username: postgres
Password: postgres
```

Select the view:

```text
analytics.vw_cases_powerbi
```

The dashboard file is located in:

```text
powerbi/document_intelligence_dashboard.pbix
```

---

## Testing

Run tests with:

```bash
pytest
```

The test suite validates the document parser and includes a specific case for empty fields to ensure the parser does not incorrectly capture the following line as a value.

---

## Data Privacy

This repository does not publish real administrative records, institutional documents, personal data, internal codes, signatures, or confidential observations.

The public version uses synthetic documents that preserve the structure and complexity of real administrative workflows without exposing sensitive information.

This approach demonstrates realistic document intelligence and analytics engineering capabilities while respecting privacy and confidentiality.

---

## Current Status

Completed:

- [x] Initial project structure
- [x] Synthetic document generation
- [x] Python extraction pipeline
- [x] PDF, Word, and TXT document reading
- [x] Data quality validation
- [x] Processed CSV output
- [x] PostgreSQL Docker setup
- [x] Staging table load
- [x] Analytics dimensional model
- [x] Power BI reporting view
- [x] Power BI dashboard with four pages
- [x] Dashboard screenshots
- [x] Warm executive Power BI design system

Planned:

- [ ] Add dbt transformations
- [ ] Add Airflow orchestration
- [ ] Add Azure Blob Storage integration
- [ ] Add Azure Document Intelligence version
- [ ] Add GitHub Actions validation workflow
- [ ] Add automated data quality report
- [ ] Add deployment notes for cloud environments

---

## Future Improvements

Planned improvements include:

- replacing SQL scripts with dbt models;
- adding Airflow orchestration for scheduled runs;
- creating a cloud version using Azure Blob Storage and Azure SQL or PostgreSQL;
- integrating Azure Document Intelligence for advanced document extraction;
- adding CI checks with GitHub Actions;
- improving data quality logging and audit trails;
- adding incremental loads;
- adding a production-style monitoring layer;
- creating a Power BI Service deployment version.

---

## Engineering Highlights

This project covers the full analytical workflow from document ingestion to reporting:

- document processing;
- Python automation;
- data extraction;
- data quality validation;
- PostgreSQL modeling;
- SQL transformations;
- dimensional modeling;
- Power BI reporting;
- dashboard design;
- operational analytics;
- privacy-aware data handling.

---

## License

This project is intended for educational and technical demonstration purposes. The dataset is synthetic and does not represent real individuals, institutions, or confidential administrative records.
