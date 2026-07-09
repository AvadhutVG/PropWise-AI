from pathlib import Path
import pandas as pd


def save_dataframe(df: pd.DataFrame, filename: str):
    """
    Save a DataFrame to the processed data folder.
    """

    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename

    df.to_csv(output_path, index=False)

    print(f"Dataset saved to: {output_path}")