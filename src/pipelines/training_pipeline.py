from src.data.clean_data import clean_dataset
from src.features.create_features import create_features
from src.outliers.remove_outliers import remove_sqft_per_bhk_outliers
from src.outliers.location_outliers import analyze_locations
from src.features.location_features import group_rare_locations
from src.outliers.price_outliers import remove_price_per_sqft_outliers
from src.outliers.price_outliers import remove_price_per_sqft_outliers
from src.outliers.bathroom_outliers import remove_bathroom_outliers
from src.models.prepare_data import prepare_features
from src.models.train_test_split import split_data
from src.models.train_linear_regression import train_linear_regression
from src.models.evaluate_model import evaluate_model

def run_pipeline():

    df = clean_dataset()

    df = create_features(df)

    df = remove_sqft_per_bhk_outliers(df)

    df = group_rare_locations(df)

    df = remove_price_per_sqft_outliers(df)
    df = remove_bathroom_outliers(df)
    #analyze_locations(df)
    X, y = prepare_features(df)

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    model = train_linear_regression(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    return X_train, X_test, y_train, y_test