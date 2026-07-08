from src.data.load_data import load_dataset


def inspect_dataset():
    df = load_dataset()

    print("=" * 80)
    print("DATASET SHAPE")
    print("=" * 80)
    print(df.shape)

    print("\n" + "=" * 80)
    print("COLUMN NAMES")
    print("=" * 80)
    print(df.columns.tolist())

    print("\n" + "=" * 80)
    print("DATA TYPES")
    print("=" * 80)
    print(df.dtypes)

    print("\n" + "=" * 80)
    print("MISSING VALUES")
    print("=" * 80)
    print(df.isnull().sum())

    print("\n" + "=" * 80)
    print("DUPLICATE ROWS")
    print("=" * 80)
    print(df.duplicated().sum())

    print("\n" + "=" * 80)
    print("FIRST 5 ROWS")
    print("=" * 80)
    print(df.head())