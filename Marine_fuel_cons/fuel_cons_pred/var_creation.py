import random
from . import dict

#Creating variables based of the input from the user (these variables in a real aplication will be replaced by the ship's ADLM system)
def create_var_inherited(rpm, aft_draft, fore_draft, heading):   
    MIDDLE_DRAFT_P = (aft_draft + fore_draft)/2
    MIDDLE_DRAFT_S = (aft_draft + fore_draft)/2
    WATER_DEPTH = 80
    if 0 <= rpm < 10:
        TURBOCHARGER_SPEED = 850
        SHAFT_POWER = 180
        PROPELLER_SHAFT_THRUST = -60
        PROPELLER_SHAFT_TORQUE = 80
    elif 10 <= rpm < 20:
        TURBOCHARGER_SPEED = 1300
        SHAFT_POWER = 500
        PROPELLER_SHAFT_THRUST = -100
        PROPELLER_SHAFT_TORQUE = 120
    elif 20 <= rpm < 30:
        TURBOCHARGER_SPEED = 2600
        SHAFT_POWER = 900
        PROPELLER_SHAFT_THRUST = -130
        PROPELLER_SHAFT_TORQUE = 220
    elif 30 <= rpm < 40:
        TURBOCHARGER_SPEED = 3100
        SHAFT_POWER = 1100
        PROPELLER_SHAFT_THRUST = -160
        PROPELLER_SHAFT_TORQUE = 260
    elif 40 <= rpm < 50:
        TURBOCHARGER_SPEED = 4500
        SHAFT_POWER = 1600
        PROPELLER_SHAFT_THRUST = -200
        PROPELLER_SHAFT_TORQUE = 340
    elif 50 <= rpm < 60:
        TURBOCHARGER_SPEED = 6200
        SHAFT_POWER = 2900
        PROPELLER_SHAFT_THRUST = -350
        PROPELLER_SHAFT_TORQUE = 500
    elif 60 <= rpm < 70:
        TURBOCHARGER_SPEED = 9500
        SHAFT_POWER = 4500
        PROPELLER_SHAFT_THRUST = -500
        PROPELLER_SHAFT_TORQUE = 650
    elif 70 <= rpm < 80:
        TURBOCHARGER_SPEED = 11000
        SHAFT_POWER = 6000
        PROPELLER_SHAFT_THRUST = -600
        PROPELLER_SHAFT_TORQUE = 750
    elif 80 <= rpm < 90:
        TURBOCHARGER_SPEED = 13500
        SHAFT_POWER = 8000
        PROPELLER_SHAFT_THRUST = -650
        PROPELLER_SHAFT_TORQUE = 860
    else:
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
    return (TURBOCHARGER_SPEED, WATER_DEPTH, PROPELLER_SHAFT_THRUST, PROPELLER_SHAFT_TORQUE, MIDDLE_DRAFT_P,
            SHAFT_POWER, MIDDLE_DRAFT_S)

#Creating dummy variables from the mean value of the training dataset
def create_var_dummy():
    FUEL_OIL_FLOW_SUPPLY = dict.dict_of_attributes['FUEL OIL FLOW SUPPLY'][0]
    FUEL_OIL_FLOW_RETURN = dict.dict_of_attributes['FUEL OIL FLOW RETURN'][0]
    FUEL_OIL_SUPPLY_TEMPERATURE = dict.dict_of_attributes['FUEL OIL SUPPLY TEMPERATURE'][0]
    FUEL_OIL_RETURN_TEMPERATURE = dict.dict_of_attributes['FUEL OIL RETURN TEMPERATURE'][0]
    INTERMEDIATE_SHAFT_BEARING_TEMP = dict.dict_of_attributes['INTERMEDIATE SHAFT BEARING TEMP'][0]
    FUEL_OIL_INLET_PRESSURE = dict.dict_of_attributes['FUEL OIL INLET PRESSURE'][0]
    FUEL_OIL_INLET_TEMPERATURE = dict.dict_of_attributes['FUEL OIL INLET TEMPERATURE'][0]
    TURBOCHARGER_EXH_EXH_GAS_INLET_TEMP = dict.dict_of_attributes['TURBOCHARGER EXH EXH GAS INLET TEMP'][0]
    TURBOCHARGER_EXH_EXH_GAS_OUTLET_TEMP = dict.dict_of_attributes['TURBOCHARGER EXH EXH GAS OUTLET TEMP'][0]
    THRUST_BEARING_TEMPERATURE = dict.dict_of_attributes['THRUST BEARING TEMPERATURE'][0]
    STERN_TUBE_BEARING_TEMPERATURE = dict.dict_of_attributes['STERN TUBE BEARING TEMPERATURE'][0]
    THRUST_MAIN_BEARING_TEMP = dict.dict_of_attributes['THRUST MAIN BEARING TEMP'][0]
    return (FUEL_OIL_FLOW_SUPPLY, FUEL_OIL_FLOW_RETURN, STERN_TUBE_BEARING_TEMPERATURE, FUEL_OIL_RETURN_TEMPERATURE, 
            FUEL_OIL_SUPPLY_TEMPERATURE, TURBOCHARGER_EXH_EXH_GAS_INLET_TEMP,TURBOCHARGER_EXH_EXH_GAS_OUTLET_TEMP, 
            FUEL_OIL_INLET_TEMPERATURE, FUEL_OIL_INLET_PRESSURE, INTERMEDIATE_SHAFT_BEARING_TEMP, THRUST_BEARING_TEMPERATURE,
            THRUST_MAIN_BEARING_TEMP)

#Creating dummy enviromental variables in order to show the flustration in ship's fuel consuption. (These variables in a real application will be consumed by a weather API)
def create_random_env_vars():
    AIR_PRESSURE_AT_SEA_LEVEL = random.randrange(1006, 1018)
    AIR_TEMPERATURE_AT_10M = random.randrange(17, 27)
    CURRENT_DIRECTION = random.randrange(90, 259)
    CURRENT_SPEED = random.randrange(0, 1)
    EASTWARD_CURRENT = random.randrange(-1, 1)
    WAVE_HEIGHT = random.randrange(0, 4)
    WAVE_DIRECTION = random.randrange(135, 265)
    WAVE_LENGTH = random.randrange(24, 143)
    NORTHWARD_CURRENT = random.randrange(-1, 1)
    SEA_TEMPERATURE = random.randrange(17, 28)
    SIGNIFICANT_WAVE_HEIGHT = random.randrange(0, 2)
    SWELL_WAVE_HEIGHT = random.randrange(0, 3)
    SWELL_WAVE_DIRECTION = random.randrange(133, 267)
    SWELL_WAVE_LENGTH = random.randrange(34, 175)
    SWELL_SIGNIFICANT_WAVE_HEIGHT = random.randrange(0, 2)
    WIND_RELATIVE_DIRECTION = random.randrange(92, 264)
    WIND_RELATIVE_SPEED = random.randrange(2, 7)
    WINDWAVE_WAVE_HEIGHT = random.randrange(0, 2)
    WINDWAVE_WAVE_DIRECTION = random.randrange(98, 266)
    WINDWAVE_WAVE_LENGTH = random.randrange(0, 43)
    WINDWAVE_WAVE_HEIGHT_1 = random.randrange(0, 8)
    return (WAVE_DIRECTION, WINDWAVE_WAVE_DIRECTION, SWELL_WAVE_DIRECTION, CURRENT_DIRECTION, WAVE_HEIGHT,  
            SWELL_WAVE_HEIGHT, SIGNIFICANT_WAVE_HEIGHT, SWELL_SIGNIFICANT_WAVE_HEIGHT,WINDWAVE_WAVE_HEIGHT,
            CURRENT_SPEED, EASTWARD_CURRENT, WIND_RELATIVE_DIRECTION, SWELL_WAVE_LENGTH, NORTHWARD_CURRENT,
            AIR_TEMPERATURE_AT_10M, WAVE_LENGTH, WINDWAVE_WAVE_HEIGHT_1, SEA_TEMPERATURE, AIR_PRESSURE_AT_SEA_LEVEL,
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