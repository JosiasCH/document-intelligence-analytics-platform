# Architecture

## MVP architecture

```text
Synthetic PDF/DOCX/TXT documents
        ↓
Text extraction module
        ↓
Pattern-based field parser
        ↓
Data validation module
        ↓
Clean CSV output
        ↓
PostgreSQL staging tables
        ↓
SQL analytical queries
        ↓
Power BI dashboard
```

## Future production architecture

```text
Azure Blob Storage
        ↓
Azure Document Intelligence
        ↓
Python ingestion service
        ↓
Raw tables
        ↓
dbt transformations
        ↓
Data quality tests
        ↓
Dimensional model
        ↓
Power BI Service
        ↓
Business users
```

## Design principles

- Privacy by design.
- Reproducible processing.
- Clear separation between raw, staging, and analytical layers.
- Data quality checks before reporting.
- Documentation-first development.
- BI-ready dimensional modeling.
