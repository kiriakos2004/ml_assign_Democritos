import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, mutual_info_regression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import HistGradientBoostingRegressor


#Read Dataset
data = pd.read_csv("dataset.csv", sep=";")

#Create a list of column names (to find out if there is something to dispose)
def list_column_names():
    column_names = []
    for column in data.columns:
        column_names.append(column)
        print(column_names)
#list_column_names()

# Dropping attributes that dont contribute in engine's fuel consumption (step of datapreprocessing with the use of domain expertise)
drop_list = ['DATETIME', 'MAGNETIC COURSE OVER GROUND', 'MAGNETIC VARIATION', 'MAIN ENGINE FUEL INDEX', 
             'MAIN ENGINE SCAVENGE AIR RECEIVER TEMPERATURE', 'TURBOCHARGER LUB OIL INLET PRESSURE', 
             'TURBOCHARGER LUB OIL INLET TEMPERATURE']
data = data.drop(drop_list, axis=1)

#Assigning the label
label = "ME FUEL CONSUMPTION"

#keep the instances where the label is not NaN
null_label = pd.notnull(data[label])
data = data[null_label]

#Splitting dataset in label and attributes
y = data.loc[:, label]
X = data.loc[:, data.columns != label]

#Impute missing values using the mean of each attribute (naive imputing method)
X = X.fillna(X.mean())

#As a feature selection step we may choose to keep the n (40) number of attributes with the highest dependency to label
#X = SelectKBest(mutual_info_regression, k=40).fit_transform(X, y)

#Splitting in Train and Test (due to sufficent number of instances for training we held out 20% of data for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=112)

#The values between different data attributes span to wide range so it is beneficcial for algorithm converge to normalize the data
scaler = preprocessing.StandardScaler().fit(X_train)
X_train_transformed = scaler.transform(X_train)
X_test_transformed = scaler.transform(X_test)

#Hyperparameter tuning using GridSearch in the training dataset for SVC regressor
def svc_regressor():
    hyperparam_grid = {'C': [0.1, 1, 10, 100], 'gamma': [0.01, 0.5, 1], 'epsilon': [0.01, 0.1, 1]}
    svr_reg = SVR(kernel='rbf')
    grid_search = GridSearchCV(svr_reg, hyperparam_grid, cv=10, verbose=2, pre_dispatch='2*n_jobs', n_jobs=4)
    grid_search.fit(X_train_transformed, y_train)
    svc_hyp_list = [{grid_search.best_params_['C']},
                    {grid_search.best_params_['gamma']},
                    {grid_search.best_params_['epsilon']}]
    print(f"The best C value: {grid_search.best_params_['C']}")
    print(f"The best gamma value is : {grid_search.best_params_['gamma']}")
    print(f"The best epsilon value: {grid_search.best_params_['epsilon']}")
    return svc_hyp_list
svc_regressor()

#Hyperparameter tuning using GridSearch in the training dataset for GradientBoosting regressor
def gb_regressor():
    hyperparam_grid = {
    "learning_rate": [0.01, 0.1],
    "max_depth": [5, 10, 20],
    "l2_regularization": [True, False]}
    hist_gb_reg = HistGradientBoostingRegressor(
        max_iter=500, 
        loss="squared_error", 
        early_stopping='auto', 
        scoring='loss', 
        n_iter_no_change=5, 
        tol=1e-5, 
        verbose=2)
    grid_search = GridSearchCV(hist_gb_reg, hyperparam_grid, cv=10)
    grid_search.fit(X_train_transformed, y_train)
    gb_regressor_hyp_list = [grid_search.best_params_['learning_rate'], 
                             {grid_search.best_params_['max_depth']}, 
                             {grid_search.best_params_['l2_regularization']}]
    print(f"The best learning_rate value is: {grid_search.best_params_['learning_rate']}")
    print(f"The best max_depth value: {grid_search.best_params_['max_depth']}")
    print(f"The l2_regularization must be set to: {grid_search.best_params_['l2_regularization']}")
    return gb_regressor_hyp_list
#gb_regressor()
#The best hyperparameters are: (learning_rate=0.1, max_depth=10, l2_regularization=True)

#validate the metrics over cross validation to check svc_regressor consistency
def cross_val_svc_regressor(C, gamma, epsilon):
    tuned_svc = SVR(kernel='rbf', C=C, gamma=gamma, epsilon=epsilon, random_state=112)
    scores = cross_val_score(tuned_svc, X, y, cv=10, scoring='neg_root_mean_squared_error')
    print(scores)
    return scores
#cross_val_svc_regressor(svc_regressor()[0], svc_regressor()[1], svc_regressor()[2])

#validate the metrics over cross validation to check GradientBoosting consistency
def cross_val_gb_regressor(learning_rate, max_depth, l2_regularization):
    tuned_gb = HistGradientBoostingRegressor(learning_rate= learning_rate,
                   max_depth= max_depth,
                   l2_regularization= l2_regularization,
                    max_iter=500, 
                    loss="squared_error", 
                    early_stopping='auto', 
                    scoring='loss', 
                    n_iter_no_change=5, 
                    tol=1e-5,
                    random_state=112)
    scores = cross_val_score(tuned_gb, X, y, cv=10, scoring='neg_root_mean_squared_error')
    print(scores)
    return scores
#cross_val_gb_regressor(0.1, 10, True)    
