import pandas as pd


def remove_bathroom_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove houses where bathrooms exceed BHK by more than 2.
    """

    filtered_df = df[df["bath"] <= df["bhk"] + 2].copy()

    print(f"Rows Before : {len(df)}")
    print(f"Rows After  : {len(filtered_df)}")
    print(f"Rows Removed: {len(df) - len(filtered_df)}")

    return filtered_df