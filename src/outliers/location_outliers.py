import pandas as pd


def analyze_locations(df: pd.DataFrame):

    location_counts = (
        df.groupby("location")
        .size()
        .sort_values(ascending=False)
    )

    print("\nTop 10 Locations\n")
    print(location_counts.head(10))

    rare_locations = location_counts[location_counts < 10]

    print(f"\nTotal Locations : {len(location_counts)}")
    print(f"Rare Locations (<10 houses): {len(rare_locations)}")

    print(f"\nTotal Houses in Rare Locations: {rare_locations.sum()}")

    print(f"\nPercentage of Dataset: {(rare_locations.sum()/len(df))*100:.2f}%")