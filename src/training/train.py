from src.training.models.linear_regression import train_linear_regression
from src.training.models.lasso_regression import train_lasso_regression
from src.training.models.ridge_regression import train_ridge_regression
from src.training.models.decision_tree import train_decision_tree
from src.training.evaluate import evaluate_model

def train_models(X_train, X_test, y_train, y_test):
    """
    Train and evaluate all regression models.
    """

    models = {
    "Linear Regression": train_linear_regression,
    "Lasso Regression": train_lasso_regression,
    "Ridge Regression": train_ridge_regression,
    "Decision Tree": train_decision_tree,
    }

    results = {}

    for model_name, trainer in models.items():

        print(f"\nTraining {model_name}...")

        model = trainer(X_train, y_train)

        metrics = evaluate_model(
            model,
            X_test,
            y_test
        )

        results[model_name] = metrics

    return results