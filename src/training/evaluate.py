from sklearn.metrics import r2_score


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.
    """

    predictions = model.predict(X_test)

    score = r2_score(y_test, predictions)

    print(f"\nR² Score: {score:.4f}")

    return score