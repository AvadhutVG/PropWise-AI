import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["price_per_sqft"] = (df["price"] * 100000) / df["total_sqft"]

    # NEW FEATURE
    df["sqft_per_bhk"] = df["total_sqft"] / df["bhk"]

    return df