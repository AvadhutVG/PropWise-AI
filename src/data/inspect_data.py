from src.data.load_data import load_dataset


def inspect_dataset():
    df = load_dataset()

    print("\n========== SHAPE ==========")
    print(df.shape)

    print("\n========== COLUMNS ==========")
    print(df.columns.tolist())

    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())

    print("\n========== DUPLICATE ROWS ==========")
    print(df.duplicated().sum())

    print("\n========== FIRST 5 ROWS ==========")
    print(df.head())