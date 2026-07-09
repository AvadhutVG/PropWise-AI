import json
from pathlib import Path


MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)


def save_columns(columns):
    """
    Save feature column names.
    """

    columns_path = MODEL_DIR / "columns.json"

    with open(columns_path, "w") as file:
        json.dump(list(columns), file, indent=4)

    print(f"\nFeature columns saved successfully: {columns_path}")