import pickle
import numpy as np

def results(list_of_inputs):
    result_list = []
    loaded_model = pickle.load(open('C:/Users/kiria/Documents/VScode_projects/ml_assign_Democritos/Marine_fuel_cons/fuel_cons_pred/model.pkl', 'rb'))
    for i in list_of_inputs:
        i=[i]
        result = round(24*loaded_model.predict(i)[0],2)
        result_list.append(result)
    return result_list
