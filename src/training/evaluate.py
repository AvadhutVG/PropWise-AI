from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained regression model.
    """

    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = mse ** 0.5

    print("\n========== MODEL EVALUATION ==========")
    print(f"R² Score : {r2:.4f}")
    print(f"MAE      : {mae:.4f}")
    print(f"MSE      : {mse:.4f}")
    print(f"RMSE     : {rmse:.4f}")

    return {
        "R2": r2,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
    }