from src.models.train_linear_regression import train_linear_regression
from src.models.evaluate_model import evaluate_model


def train_baseline_model(X_train, X_test, y_train, y_test):
    """
    Train and evaluate the baseline Linear Regression model.
    """

    model = train_linear_regression(X_train, y_train)

    score = evaluate_model(model, X_test, y_test)

    return model, score