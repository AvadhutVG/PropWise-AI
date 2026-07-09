from sklearn.linear_model import LinearRegression


def train_linear_regression(X_train, y_train):
    """
    Train a Linear Regression model.
    """

    model = LinearRegression()

    model.fit(X_train, y_train)

    print("\nLinear Regression model trained successfully.")

    return model