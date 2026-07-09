from src.data.clean_data import clean_dataset
from src.features.create_features import create_features
from src.outliers.remove_outliers import remove_sqft_per_bhk_outliers
from src.outliers.location_outliers import analyze_locations
from src.features.location_features import group_rare_locations
from src.outliers.price_outliers import remove_price_per_sqft_outliers
from src.outliers.price_outliers import remove_price_per_sqft_outliers
from src.outliers.bathroom_outliers import remove_bathroom_outliers
from src.training.prepare_data import prepare_features
from src.training.split_data import split_data
from src.training.train import train_models
from src.training.save_model import save_model
from src.training.save_columns import save_columns

def run_pipeline():

    df = clean_dataset()

    df = create_features(df)

    df = remove_sqft_per_bhk_outliers(df)

    df = group_rare_locations(df)

    df = remove_price_per_sqft_outliers(df)
    df = remove_bathroom_outliers(df)
    #analyze_locations(df)
    X, y = prepare_features(df)

    save_columns(X.columns)

    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train, X_test, y_train, y_test = split_data(X, y)

    best_model, best_model_name, results = train_models(
    X_train,
    X_test,
    y_train,
    y_test
)

    save_model(best_model, "best_model.joblib")

    print("\n========== MODEL COMPARISON ==========")

    for model_name, metrics in results.items():
        print(f"\n{model_name}")
        print(f"R²   : {metrics['R2']:.4f}")
        print(f"MAE  : {metrics['MAE']:.4f}")
        print(f"RMSE : {metrics['RMSE']:.4f}")

    return X_train, X_test, y_train, y_test