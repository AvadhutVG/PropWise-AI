import pandas as pd


def prepare_features(df: pd.DataFrame):
    """
    Prepare dataset for model training.
    """

    columns_to_drop = [
        "price",
        "price_per_sqft",
        "size",
        "availability",
    ]

    X = df.drop(columns=columns_to_drop)
    y = df["price"]

    # One-Hot Encode location
    X = pd.get_dummies(
        X,
        columns=["location"],
        drop_first=True,
        dtype=int
    )

    print("\nFeature Matrix Shape:", X.shape)
    print("Target Shape:", y.shape)

    return X, y