from src.data.load_data import load_dataset


def convert_total_sqft(value):
    value = str(value)

    if "-" in value:
        start, end = value.split("-")
        return (float(start) + float(end)) / 2

    try:
        return float(value)

    except:
        return None


def clean_dataset():

    df = load_dataset()

    print(f"Initial Shape : {df.shape}")

    # Remove society column
    df = df.drop(columns=["society"])

    # Clean total_sqft
    df["total_sqft"] = df["total_sqft"].apply(convert_total_sqft)

    # Remove invalid sqft
    df = df.dropna(subset=["total_sqft"])

    # Remove rows with missing critical values
    # Remove rows with missing critical values
    df = df.dropna(subset=["location", "size", "bath"])

# Create BHK feature
    df["bhk"] = df["size"].str.split().str[0].astype(int)

    print(f"Final Shape : {df.shape}")

    print(df[["size", "bhk"]].head(10))

    return df