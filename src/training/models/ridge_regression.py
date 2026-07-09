from sklearn.linear_model import Ridge


def train_ridge_regression(X_train, y_train):
    """
    Train a Ridge Regression model.
    """

    model = Ridge(alpha=1.0)

    model.fit(X_train, y_train)

    print("\nRidge Regression model trained successfully.")

    return model