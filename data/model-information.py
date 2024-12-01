#Hyperparameters found through randomized_search_CV. grid_search_CV did not find a drastically better set of parameters

xgb_best_params_full = {'reg_lambda': 5, 'reg_alpha': 0.1, 'n_estimators': 150, 'max_depth': 3, 'learning_rate': 0.15250000000000002}

xgb_best_params_health = {'reg_lambda': 5, 'reg_alpha': 0, 'n_estimators': 50, 'max_depth': 5, 'learning_rate': 0.2}

xgb_best_params_care = {'reg_lambda': 10, 'reg_alpha': 1, 'n_estimators': 50, 'max_depth': 3, 'learning_rate': 0.2}

xgb_best_params_socioecon = {'reg_lambda': 5, 'reg_alpha': 0.1, 'n_estimators': 150, 'max_depth': 3, 'learning_rate': 0.15250000000000002}

xgb_best_params_environment = {'reg_lambda': 1, 'reg_alpha': 1, 'n_estimators': 100, 'max_depth': 3, 'learning_rate': 0.105}

xgb_best_params_demographic = {'reg_lambda': 5, 'reg_alpha': 0.1, 'n_estimators': 150, 'max_depth': 3, 'learning_rate': 0.15250000000000002}

#number of neighbors to use in the kNN imputer
n_neighbors = 10 

'''The final algorithm we are using is as follows:

final_xgb_model = Pipeline([('impute', KNNImputer(n_neighbors=10)),
                       ('xgb', XGBRegressor(**xgb_best_params_full))])'''