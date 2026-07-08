from src.data.load_data import load_dataset


def create_bhk_feature():
    df = load_dataset()

    # Extract first number from the size column
    df["bhk"] = df["size"].str.split().str[0].astype(float)

    print(df[["size", "bhk"]].head(15))

    return df