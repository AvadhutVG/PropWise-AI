from src.training.models.linear_regression import train_linear_regression
from src.training.models.lasso_regression import train_lasso_regression
from src.training.models.ridge_regression import train_ridge_regression
from src.training.tuning.grid_search import tune_decision_tree
from src.training.evaluate import evaluate_model


def train_models(X_train, X_test, y_train, y_test):
    """
    Train and evaluate all regression models.
    """

    models = {
        "Linear Regression": train_linear_regression,
        "Lasso Regression": train_lasso_regression,
        "Ridge Regression": train_ridge_regression,
        "Tuned Decision Tree": tune_decision_tree,
    }

    results = {}

    trained_models = {}

    for model_name, trainer in models.items():

        print(f"\nTraining {model_name}...")

        model = trainer(X_train, y_train)

        metrics = evaluate_model(
            model,
            X_test,
            y_test,
        )

        results[model_name] = metrics
        trained_models[model_name] = model

    best_model_name = max(
        results,
        key=lambda model: results[model]["R2"]
    )

    best_model = trained_models[best_model_name]

    print("\n========== BEST MODEL ==========")
    print(best_model_name)
    print(f"R² Score : {results[best_model_name]['R2']:.4f}")

    return best_model, best_model_name, results