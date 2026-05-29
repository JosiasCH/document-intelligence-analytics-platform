from pathlib import Path

import pandas as pd

from src.extract.extract_text import extract_text
from src.extract.parse_case_document import parse_case_document
from src.quality.validate_cases import validate_record
from src.utils.config import PROCESSED_OUTPUT_PATH, SAMPLE_DOCS_PATH

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}


def run_pipeline(input_dir: Path = SAMPLE_DOCS_PATH, output_path: Path = PROCESSED_OUTPUT_PATH) -> pd.DataFrame:
    records = []
    quality_issues = []

    for file_path in sorted(input_dir.iterdir()):
        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        text = extract_text(file_path)
        record = parse_case_document(text, source_file=file_path.name)
        records.append(record)
        quality_issues.extend(validate_record(record))

    if not records:
        raise RuntimeError(f"No supported documents found in {input_dir}")

    df = pd.DataFrame(records)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    quality_path = output_path.parent / "data_quality_issues.csv"
    pd.DataFrame(quality_issues).to_csv(quality_path, index=False)

    print(f"Processed documents: {len(df)}")
    print(f"Clean output: {output_path}")
    print(f"Quality issues output: {quality_path}")

    return df


if __name__ == "__main__":
    run_pipeline()
