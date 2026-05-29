from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

from src.utils.config import DATABASE_URL, PROCESSED_OUTPUT_PATH


def load_cases_to_postgres(csv_path: Path = PROCESSED_OUTPUT_PATH) -> None:
    if not csv_path.exists():
        raise FileNotFoundError(f"Processed file not found: {csv_path}")

    df = pd.read_csv(csv_path)
    engine = create_engine(DATABASE_URL)

    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS staging;"))
        df.to_sql(
            "stg_cases",
            conn,
            schema="staging",
            if_exists="replace",
            index=False,
        )

    print(f"Loaded {len(df)} records into staging.stg_cases")


if __name__ == "__main__":
    load_cases_to_postgres()
