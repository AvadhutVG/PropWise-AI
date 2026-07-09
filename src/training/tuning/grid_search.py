from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor


def tune_decision_tree(X_train, y_train):
    """
    Tune Decision Tree hyperparameters using GridSearchCV.
    """

    parameters = {
        "max_depth": [5, 10, 15, 20],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    }

    grid = GridSearchCV(
        estimator=DecisionTreeRegressor(random_state=42),
        param_grid=parameters,
        cv=5,
        scoring="r2",
        n_jobs=-1,
    )

    grid.fit(X_train, y_train)

    print("\n========== BEST DECISION TREE ==========")
    print("Best Score :", round(grid.best_score_, 4))
    print("Best Params:", grid.best_params_)

    return grid.best_estimator_