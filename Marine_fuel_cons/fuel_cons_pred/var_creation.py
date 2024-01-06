import random
from . import dict

#Creating variables based of the input from the user (these variables in a real aplication will be replaced by the ship's ADLM system)
def create_var_inherited(aft_draft, fore_draft):   
    MIDDLE_DRAFT_P = (aft_draft + fore_draft)/2
    MIDDLE_DRAFT_S = (aft_draft + fore_draft)/2
    WATER_DEPTH = 80
    return (WATER_DEPTH, MIDDLE_DRAFT_P, MIDDLE_DRAFT_S)

#Creating dummy variables from the mean value of the training dataset
def create_var_dummy():
    INTERMEDIATE_SHAFT_BEARING_TEMP = dict.dict_of_attributes['INTERMEDIATE SHAFT BEARING TEMP'][0]
    FUEL_OIL_INLET_PRESSURE = dict.dict_of_attributes['FUEL OIL INLET PRESSURE'][0]
    FUEL_OIL_INLET_TEMPERATURE = dict.dict_of_attributes['FUEL OIL INLET TEMPERATURE'][0]
    THRUST_BEARING_TEMPERATURE = dict.dict_of_attributes['THRUST BEARING TEMPERATURE'][0]
    STERN_TUBE_BEARING_TEMPERATURE = dict.dict_of_attributes['STERN TUBE BEARING TEMPERATURE'][0]
    THRUST_MAIN_BEARING_TEMP = dict.dict_of_attributes['THRUST MAIN BEARING TEMP'][0]
    return (STERN_TUBE_BEARING_TEMPERATURE, FUEL_OIL_INLET_TEMPERATURE, FUEL_OIL_INLET_PRESSURE, 
            INTERMEDIATE_SHAFT_BEARING_TEMP, THRUST_BEARING_TEMPERATURE, THRUST_MAIN_BEARING_TEMP)

#Creating dummy enviromental variables in order to show the flustration in ship's fuel consuption. (These variables in a real application will be consumed by a weather API)
def create_random_env_vars():
    AIR_PRESSURE_AT_SEA_LEVEL = random.randrange(1013, 1017)
    AIR_TEMPERATURE_AT_10M = random.randrange(23, 26)
    EASTWARD_CURRENT = random.randrange(-1, 1)
    WAVE_HEIGHT = random.randrange(3, 4)
    WAVE_DIRECTION = random.randrange(120, 180)
    WAVE_LENGTH = random.randrange(108, 142)
    NORTHWARD_CURRENT = random.randrange(-1, 1)
    SEA_TEMPERATURE = random.randrange(24, 27)
    SIGNIFICANT_WAVE_HEIGHT = random.randrange(1, 2)
    SWELL_WAVE_HEIGHT = random.randrange(2, 3)
    SWELL_WAVE_DIRECTION = random.randrange(140, 200)
    SWELL_WAVE_LENGTH = random.randrange(130, 160)
    SWELL_SIGNIFICANT_WAVE_HEIGHT = random.randrange(1, 2)
    WIND_RELATIVE_DIRECTION = random.randrange(70, 210)
    WIND_RELATIVE_SPEED = random.randrange(3, 6)
    WINDWAVE_WAVE_HEIGHT = random.randrange(1, 2)
    WINDWAVE_WAVE_DIRECTION = random.randrange(70, 160)
    WINDWAVE_WAVE_LENGTH = random.randrange(23, 26)
    return (WAVE_DIRECTION, WINDWAVE_WAVE_DIRECTION, SWELL_WAVE_DIRECTION, WAVE_HEIGHT,  
            SWELL_WAVE_HEIGHT, SIGNIFICANT_WAVE_HEIGHT, SWELL_SIGNIFICANT_WAVE_HEIGHT,WINDWAVE_WAVE_HEIGHT,
            EASTWARD_CURRENT, WIND_RELATIVE_DIRECTION, SWELL_WAVE_LENGTH, NORTHWARD_CURRENT,
            AIR_TEMPERATURE_AT_10M, WAVE_LENGTH, SEA_TEMPERATURE, AIR_PRESSURE_AT_SEA_LEVEL,
            WIND_RELATIVE_SPEED, WINDWAVE_WAVE_LENGTH)

#this function combines all of the above and creates a nested list with data for prediction for each day (which equals to duration)
def create_data_for_pred(duration, rpm, aft_draft, fore_draft, heading):
    list_for_predict = []
    i=1
    while i<= duration:
        dummy_list=[]
        for j in range(3):
            dummy_list.append(create_random_env_vars()[j])
        dummy_list.append(create_var_dummy()[0])
        dummy_list.append(create_random_env_vars()[3])
        dummy_list.append(create_var_dummy()[1])
        dummy_list.append(create_var_dummy()[2])
        dummy_list.append(create_random_env_vars()[4])
        dummy_list.append(create_random_env_vars()[5])
        dummy_list.append(create_var_dummy()[3])
        dummy_list.append(create_random_env_vars()[6])
        dummy_list.append(create_var_dummy()[4])
        dummy_list.append(create_random_env_vars()[7])
        dummy_list.append(create_var_dummy()[5])
        dummy_list.append(create_var_dummy()[6])
        for k in range(8,11):
            dummy_list.append(create_random_env_vars()[k])
        dummy_list.append(create_var_dummy()[7])
        dummy_list.append(fore_draft)
        for l in range(11,17):
            dummy_list.append(create_random_env_vars()[l])
        dummy_list.append(aft_draft)
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[0])
        dummy_list.append(create_random_env_vars()[17])
        dummy_list.append(create_var_dummy()[8])
        dummy_list.append(create_random_env_vars()[18])
        for m in range(1,4):
            dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[m])
        dummy_list.append(create_var_dummy()[9])
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[4])
        dummy_list.append(create_random_env_vars()[19])
        dummy_list.append(heading)
        dummy_list.append(create_var_dummy()[10])
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[5])
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[6])
        dummy_list.append(create_var_dummy()[11])
        dummy_list.append(create_random_env_vars()[20])
        dummy_list.append(rpm)
        list_for_predict.append(dummy_list)
        i+=1
    return (list_for_predict)
create_data_for_pred(10, 40, 11.33, 9.51, 161.33)

#Creating a list of labels to be used in chart
def create_labels(duration):
    list_of_labels = [str(n) for n in range(1, int(duration)+1)]
    list_of_labels = [f"Fuel cons for day: {x}" for x in list_of_labels]
    return list_of_labels