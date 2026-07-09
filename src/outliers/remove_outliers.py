import pandas as pd


def remove_sqft_per_bhk_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove houses with less than 300 sqft per BHK.
    """

    original_rows = len(df)

    df = df[df["sqft_per_bhk"] >= 300].copy()

    removed = original_rows - len(df)

    print(f"Rows Removed : {removed}")
    print(f"Remaining Rows : {len(df)}")

    return df