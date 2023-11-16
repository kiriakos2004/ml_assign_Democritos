import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor

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

#keep the instances where the label is not NaA

#Splitting dataset in label and 
y = data.loc[:, label]
X = data.loc[:, data.columns != label]





