from sklearn.linear_model import Lasso


def train_lasso_regression(X_train, y_train):
    """
    Train a Lasso Regression model.
    """

    model = Lasso(alpha=0.1)

    model.fit(X_train, y_train)

    print("\nLasso Regression model trained successfully.")

    return model