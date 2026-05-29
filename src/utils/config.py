from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SAMPLE_DOCS_PATH = PROJECT_ROOT / os.getenv("SAMPLE_DOCS_PATH", "data/sample")
PROCESSED_OUTPUT_PATH = PROJECT_ROOT / os.getenv("PROCESSED_OUTPUT_PATH", "data/processed/cases_extracted.csv")
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/doc_intelligence"
)
