import pandas as pd

from src.prediction.utils import load_model, load_columns
from src.prediction.loader import model, columns

model = load_model()
columns = load_columns()


def predict_price(
    location,
    total_sqft,
    bath,
    balcony,
    bhk,
):
    """
    Predict house price.
    """

    data = pd.DataFrame(
        0,
        index=[0],
        columns=columns
    )

    data["total_sqft"] = total_sqft
    data["bath"] = bath
    data["balcony"] = balcony
    data["bhk"] = bhk

    location_column = f"location_{location}"

    if location_column in data.columns:
        data[location_column] = 1

    prediction = model.predict(data)[0]

    return round(prediction, 2)