import pandas as pd


def remove_price_per_sqft_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove price_per_sqft outliers for each location using mean ± std.
    """

    cleaned_df = pd.DataFrame()

    for location, location_df in df.groupby("location"):

        mean = location_df["price_per_sqft"].mean()
        std = location_df["price_per_sqft"].std()

        filtered = location_df[
            (location_df["price_per_sqft"] >= (mean - std)) &
            (location_df["price_per_sqft"] <= (mean + std))
        ]

        cleaned_df = pd.concat([cleaned_df, filtered], ignore_index=True)

    print(f"Rows Before : {len(df)}")
    print(f"Rows After  : {len(cleaned_df)}")
    print(f"Rows Removed: {len(df) - len(cleaned_df)}")

    return cleaned_df