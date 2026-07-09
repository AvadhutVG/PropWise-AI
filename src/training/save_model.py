import joblib
from pathlib import Path


MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)


def save_model(model, filename):
    """
    Save a trained model to the models directory.
    """

    model_path = MODEL_DIR / filename

    joblib.dump(model, model_path)

    print(f"\nModel saved successfully: {model_path}")