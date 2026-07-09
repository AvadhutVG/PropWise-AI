import pandas as pd


def group_rare_locations(df: pd.DataFrame, min_count: int = 10) -> pd.DataFrame:
    """
    Replace locations that appear fewer than min_count times with 'Other'.
    """

    df = df.copy()

    location_counts = df["location"].value_counts()

    rare_locations = location_counts[location_counts < min_count].index

    df["location"] = df["location"].replace(rare_locations, "Other")

    print(f"Grouped {len(rare_locations)} rare locations into 'Other'.")

    print(f"Remaining unique locations: {df['location'].nunique()}")

    return df