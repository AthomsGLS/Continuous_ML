from sklearn.ensemble import RandomForestRegressor

def model_train(X_train, y_train, seed):
    # Fit a model on the train section
    regr = RandomForestRegressor(max_depth=2, random_state=seed)
    regr.fit(X_train, y_train)

    return regr
