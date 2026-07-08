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

    # Create cleaned sqft column
    df["total_sqft"] = df["total_sqft"].apply(convert_total_sqft)

    original_rows = len(df)

    # Remove rows with invalid sqft
    df = df.dropna(subset=["total_sqft"])

    removed_rows = original_rows - len(df)

    print(f"Original Rows : {original_rows}")
    print(f"Removed Rows  : {removed_rows}")
    print(f"Remaining Rows: {len(df)}")

    return df