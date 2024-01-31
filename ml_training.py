import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import pickle
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, mutual_info_regression, SelectPercentile, f_regression
from sklearn.metrics import mean_squared_error, max_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import HistGradientBoostingRegressor, BaggingRegressor
from sklearn.neighbors import KNeighborsRegressor

#Read Datasets
data = pd.read_csv("dataset.csv", sep=";")

test_data= pd.read_csv("dataset_test.csv", sep=";")

#Create a list of column names (to find out if there is something to dispose)
def list_column_names():
    column_names = []
    for column in data.columns:
        column_names.append(column)
    print(column_names)
#list_column_names()
        

# Dropping attributes that dont contribute in engine's fuel consumption (step of data preprocessing with the use of domain expertise)
drop_list = ['DATETIME', 'MAGNETIC COURSE OVER GROUND', 'MAGNETIC VARIATION', 'MAIN ENGINE FUEL INDEX', 
             'MAIN ENGINE SCAVENGE AIR RECEIVER TEMPERATURE', 'TURBOCHARGER LUB OIL INLET PRESSURE', 
             'TURBOCHARGER LUB OIL INLET TEMPERATURE']

data = data.drop(drop_list, axis=1)
test_data = test_data.drop(drop_list, axis=1)

#Assigning the label
label = "ME FUEL CONSUMPTION"

#keep the instances where the label is not NaN
null_label = pd.notnull(data[label])
data = data[null_label]

null_label_test = pd.notnull(test_data[label])
test_data = test_data[null_label_test]

#Splitting dataset in label and attributes
y = data.loc[:, label]
X = data.loc[:, data.columns != label]

y_test = test_data.loc[:, label]
X_test = test_data.loc[:, test_data.columns != label]

#Impute missing values using the mean of each attribute (naive imputing method)
X = X.fillna(X.mean())

X_test = X_test.fillna(X_test.mean())

#find out the 'mean' and 'std' of the different attributes and save it as stats.txt
#we will use mean value as default for all inputs that the user doesn't fill in form (or we will not put in form)
def statistics():
    Statistics = X.describe().loc[['mean', 'std']]
    dict_temp = Statistics.to_dict('split')
    names_list = dict_temp['columns']
    mean_list = dict_temp['data'][0]
    round_mean_list = [round(num_mean, 2) for num_mean in mean_list]
    std_list = dict_temp['data'][1]
    round_std_list = [round(num_std, 2) for num_std in std_list]
    l = []
    l.extend([list(a) for a in zip(round_mean_list, round_std_list)])
    statistics_dict = dict(zip(names_list, l))
    with open('stats.txt', 'w') as f:
        f.write(str(statistics_dict))
    return statistics_dict
#statistics()

#As a preprocessing step we should visualize data in order to improve insights of dataset
def vis_attr():
    attribute = input("Please input one of the attribute titles dispalyed in 'dataset_attributes.txt': ")
    width = 12
    height = 6
    sns.set(rc = {'figure.figsize':(width,height)})
    sns.lineplot(data=X[attribute], color="#62466B").set(title=f'Lineplot of attribute: {attribute}')
    sns.set_style("dark")
    plt.show()
#vis_attr()

#After the visualization of the data we can figure out that more attributes can be dropped due to high correlation with other attributes
#We can also drop TRIM as a feature engineering step as it arises from AFT and FORE draught
vis_drop_list = ['PROPELLER SHAFT REVOLUTIONS', 'LONGITUDINAL GROUND SPEED', 'LONGITUDINAL WATER SPEED','TRIM']

X = X.drop(vis_drop_list, axis=1)
X_test = X_test.drop(vis_drop_list, axis=1)

#As a feature selection step we may choose to keep the number of attributes with the highest "mutual information" to label
def vis_mutual_info():
    importances = mutual_info_regression(X,y)
    feat_importances = pd.Series(importances, X.columns[0:len(X.columns)])
    sorted_feat_importances = feat_importances.sort_values(ascending=False)
    width = 12
    height = 14
    sns.set(rc = {'figure.figsize':(width,height)})
    sns.set_style("dark")
    sns.barplot(data=sorted_feat_importances, palette="crest", orient="h").set(title='Mutual info barplot')
    plt.yticks(size=8)
    plt.show()
#vis_mutual_info()

#Keeping the attributes with the highest "mutual info" based on the observations of the vis_mutual function plot
mut_info = SelectKBest(mutual_info_regression, k=34).fit(X, y)

X = mut_info.transform(X)
X_test = mut_info.transform(X_test)

#The values between different data attributes span to wide range so it is beneficcial for algorithm converge to normalize the data
scaler = preprocessing.StandardScaler().fit(X)

X_train_transformed = scaler.transform(X)
X_test_transformed = scaler.transform(X_test)

#Hyperparameter tuning using GridSearch in the training dataset for SVC regressor
def svc_regressor():
    hyperparam_grid = {'C': [0.1, 1, 10, 100, 200, 300, 500, 1000], 'kernel':['rbf', 'linear', 'poly']}
    svr_reg = SVR(verbose=1, tol=1e-5)
    grid_search = GridSearchCV(svr_reg, hyperparam_grid, cv=10, verbose=1, scoring='neg_root_mean_squared_error', pre_dispatch='2*n_jobs', n_jobs=-1)
    grid_search.fit(X_train_transformed, y)
    svc_hyp_list = [{grid_search.best_params_['C']},
                    {grid_search.best_params_['kernel']}]
    print(f"The best C value (SVC) is: {grid_search.best_params_['C']}")
    print(f"The best kernel for (SVC) is : {grid_search.best_params_['kernel']}")
    return svc_hyp_list
#svc_regressor()
#The best hyperparameters are: (C=100, gamma=0.01,*epsilon was set by default=0.1)

#Hyperparameter tuning using GridSearch in the training dataset for GradientBoosting regressor
def gb_regressor():
    hyperparam_grid = {
    "learning_rate": [0.01, 0.1],
    "max_depth": [5, 10, 20, 30],
    "l2_regularization": [0.1, 0.01, 0.001]}
    hist_gb_reg = HistGradientBoostingRegressor(
        max_iter=500, 
        loss="squared_error", 
        early_stopping='auto', 
        scoring='loss', 
        n_iter_no_change=5, 
        tol=1e-5, 
        verbose=1)
    grid_search = GridSearchCV(hist_gb_reg, hyperparam_grid, cv=10, scoring='neg_root_mean_squared_error', n_jobs=-1)
    grid_search.fit(X_train_transformed, y)
    gb_regressor_hyp_list = [grid_search.best_params_['learning_rate'], 
                             {grid_search.best_params_['max_depth']}, 
                             {grid_search.best_params_['l2_regularization']}]
    print(f"The best learning_rate value (GB) is: {grid_search.best_params_['learning_rate']}")
    print(f"The best max_depth value (GB) is: {grid_search.best_params_['max_depth']}")
    print(f"The l2_regularization (GB) must be set to: {grid_search.best_params_['l2_regularization']}")
    return gb_regressor_hyp_list
#gb_regressor()
#The best hyperparameters are: (learning_rate=0.1, max_depth=20, l2_regularization=0.01)

#validate the metrics over cross validation for Linearregressor in order to establish prediction baseline
def cross_val_lnr_regressor():
    lnr = LinearRegression()
    scores = cross_val_score(lnr, X_train_transformed, y, cv=10, scoring='neg_root_mean_squared_error', n_jobs=-1)
    print(scores)
    return scores
#cross_val_lnr_regressor()

#validate the metrics over cross validation to check Bagging strategy
def cross_val_bagging_regressor():
    estimator = KNeighborsRegressor(n_neighbors=10, n_jobs=-1)
    model = model = BaggingRegressor(base_estimator=estimator, 
                                     random_state=112, 
                                     n_estimators=10, 
                                     n_jobs=-1,
                                     max_samples=100,
                                     max_features=10,
                                     verbose=1)
    scores = cross_val_score(model, X, y, cv=10, scoring='neg_root_mean_squared_error', n_jobs=-1, verbose=1)
    print(scores)
    return scores
#cross_val_bagging_regressor()

#validate the metrics over cross validation to check svc_regressor consistency
def cross_val_svc_regressor(C, kernel):
    tuned_svc = SVR(kernel=kernel, C=C)
    scores = cross_val_score(tuned_svc, X_train_transformed, y, cv=10, scoring='neg_root_mean_squared_error', n_jobs=-1)
    print(scores)
    return scores
#cross_val_svc_regressor(500, 'rbf')

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
                    tol=1e-7,
                    random_state=112)
    scores = cross_val_score(tuned_gb, X_train_transformed, y, cv=10, scoring='neg_root_mean_squared_error', n_jobs=-1)
    print(scores)
    return scores
#cross_val_gb_regressor(0.1, 5, 0.001)

#Find the maximum residual error and the mean absolute error (predicted - true) of the label using the best model in order to report the expected precision of the results ()
def find_expected_errors(learning_rate, max_depth, l2_regularization):
    model = HistGradientBoostingRegressor(learning_rate= learning_rate,
                   max_depth= max_depth,
                   l2_regularization= l2_regularization,
                    max_iter=500, 
                    loss="squared_error", 
                    early_stopping='auto', 
                    scoring='loss', 
                    n_iter_no_change=5, 
                    tol=1e-7,
                    random_state=112)
    model.fit(X_train_transformed,y)
    predictions = model.predict(X_test_transformed)  
    maximum_error = max_error(predictions, y_test)
    mean_abs_error = mean_absolute_error(predictions, y_test)
    print(f"The maximum error is:{round(maximum_error,2)}", f"The mean absolute error is:{round(mean_abs_error,2)}")
#find_expected_errors(0.1, 5, 0.001)

#training and saving the best algorithm in order to use it django framework for the actual prediction
def save_model(learning_rate, max_depth, l2_regularization):
    model = HistGradientBoostingRegressor(learning_rate= learning_rate,
                   max_depth= max_depth,
                   l2_regularization= l2_regularization,
                    max_iter=500, 
                    loss="squared_error", 
                    early_stopping='auto', 
                    scoring='loss', 
                    n_iter_no_change=5, 
                    tol=1e-5)
    model.fit(X_train_transformed, y)
    pickle.dump(model, open('model.pkl', 'wb'))
#save_model(0.1, 5, 0.001)
