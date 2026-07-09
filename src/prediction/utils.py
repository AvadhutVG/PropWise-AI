import json
import joblib
from pathlib import Path


MODEL_DIR = Path("models")


def load_model():
    """
    Load the trained model.
    """

    model_path = MODEL_DIR / "best_model.joblib"

    model = joblib.load(model_path)

    return model


def load_columns():
    """
    Load feature column names.
    """

    columns_path = MODEL_DIR / "columns.json"

    with open(columns_path, "r") as file:
        columns = json.load(file)

    return columns

def get_available_locations():
    """
    Return all available locations.
    """

    columns = load_columns()

    locations = []

    for column in columns:
        if column.startswith("location_"):
            locations.append(column.replace("location_", ""))

    locations.sort()

    return locations