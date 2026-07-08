from src.data.load_data import load_dataset


def analyze_columns():
    df = load_dataset()

    for column in df.columns:
        print("\n" + "=" * 80)
        print(f"Column : {column}")
        print("=" * 80)

        print(f"Data Type : {df[column].dtype}")

        print(f"\nUnique Values : {df[column].nunique()}")

        print("\nSample Values:")
        print(df[column].dropna().unique()[:10])