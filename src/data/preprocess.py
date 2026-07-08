from src.data.load_data import load_dataset


def convert_total_sqft(value):

    value = str(value)

    if "-" in value:
        parts = value.split("-")
        return (float(parts[0]) + float(parts[1])) / 2

    try:
        return float(value)

    except:
        return None


def inspect_failed_conversions():

    df = load_dataset()

    df["total_sqft_clean"] = df["total_sqft"].apply(convert_total_sqft)

    failed = df[df["total_sqft_clean"].isnull()]

    print(f"Failed Rows : {len(failed)}\n")

    print(failed["total_sqft"].unique())