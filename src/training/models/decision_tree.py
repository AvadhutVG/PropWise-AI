from sklearn.tree import DecisionTreeRegressor


def train_decision_tree(X_train, y_train):
    """
    Train a Decision Tree Regression model.
    """

    model = DecisionTreeRegressor(
        random_state=42
    )

    model.fit(X_train, y_train)

    print("\nDecision Tree model trained successfully.")

    return model