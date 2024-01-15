import random
from . import dict

#Creating variables based of the input from the user (these variables in a real aplication will be replaced by the ship's ADLM system)
def create_var_inherited(rpm, aft_draft, fore_draft, heading):   
    MIDDLE_DRAFT_P = (aft_draft + fore_draft)/2
    MIDDLE_DRAFT_S = (aft_draft + fore_draft)/2
    WATER_DEPTH = 80
    LIST = 0
    COURSE_OVER_GROUND = heading
    if 0 <= rpm < 10:
        SPEED_OVER_GROUND = 1
        SPEED_THROUGH_WATER = 1
    elif 10 <= rpm < 20:
        SPEED_OVER_GROUND = 3
        SPEED_THROUGH_WATER = 3
    elif 20 <= rpm < 30:
        SPEED_OVER_GROUND = 5
        SPEED_THROUGH_WATER = 5
    elif 30 <= rpm < 40:
        SPEED_OVER_GROUND = 7
        SPEED_THROUGH_WATER = 7
    elif 40 <= rpm < 50:
        SPEED_OVER_GROUND = 9
        SPEED_THROUGH_WATER = 9
    elif 50 <= rpm < 60:
        SPEED_OVER_GROUND = 10
        SPEED_THROUGH_WATER = 10
    elif 60 <= rpm < 70:
        SPEED_OVER_GROUND = 11
        SPEED_THROUGH_WATER = 11
    elif 70 <= rpm < 80:
        SPEED_OVER_GROUND = 13
        SPEED_THROUGH_WATER = 13
    elif 80 <= rpm < 90:
        SPEED_OVER_GROUND = 14
        SPEED_THROUGH_WATER = 14
    return (WATER_DEPTH, MIDDLE_DRAFT_P, MIDDLE_DRAFT_S, SPEED_OVER_GROUND,
            COURSE_OVER_GROUND, SPEED_THROUGH_WATER, LIST)

#Creating dummy variables from the mean value of the training dataset
def create_var_dummy():
    INTERMEDIATE_SHAFT_BEARING_TEMP = dict.dict_of_attributes['INTERMEDIATE SHAFT BEARING TEMP'][0]
    FUEL_OIL_INLET_PRESSURE = dict.dict_of_attributes['FUEL OIL INLET PRESSURE'][0]
    FUEL_OIL_INLET_TEMPERATURE = dict.dict_of_attributes['FUEL OIL INLET TEMPERATURE'][0]
    THRUST_BEARING_TEMPERATURE = dict.dict_of_attributes['THRUST BEARING TEMPERATURE'][0]
    STERN_TUBE_BEARING_TEMPERATURE = dict.dict_of_attributes['STERN TUBE BEARING TEMPERATURE'][0]
    THRUST_MAIN_BEARING_TEMP = dict.dict_of_attributes['THRUST MAIN BEARING TEMP'][0]
    MAIN_ENGINE_SCAVENGE_AIR_PRESSURE = dict.dict_of_attributes['MAIN ENGINE SCAVENGE AIR PRESSURE'][0]
    ME_AXIAL_VIBRATION = dict.dict_of_attributes['ME AXIAL VIBRATION'][0]
    STARBOARD_RUDDER_SENSOR = dict.dict_of_attributes['STARBOARD RUDDER SENSOR'][0]

    return (STERN_TUBE_BEARING_TEMPERATURE, FUEL_OIL_INLET_PRESSURE, THRUST_BEARING_TEMPERATURE, THRUST_MAIN_BEARING_TEMP,
            FUEL_OIL_INLET_TEMPERATURE, INTERMEDIATE_SHAFT_BEARING_TEMP, MAIN_ENGINE_SCAVENGE_AIR_PRESSURE, STARBOARD_RUDDER_SENSOR, 
            ME_AXIAL_VIBRATION, )

#Creating dummy enviromental variables in order to show the flustration in ship's fuel consuption. (These variables in a real application will be consumed by a weather API)
def create_random_env_vars():
    AIR_PRESSURE_AT_SEA_LEVEL = random.randrange(1013, 1017)
    AIR_TEMPERATURE_AT_10M = random.randrange(23, 26)
    EASTWARD_CURRENT = random.randrange(-1, 1)
    WAVE_HEIGHT = random.randrange(3, 4)
    WAVE_DIRECTION = random.randrange(120, 180)
    NORTHWARD_CURRENT = random.randrange(-1, 1)
    SWELL_WAVE_DIRECTION = random.randrange(140, 200)
    WIND_RELATIVE_DIRECTION = random.randrange(70, 210)
    WIND_RELATIVE_SPEED = random.randrange(3, 6)
    TRANSVERSE_GROUND_SPEED = random.randrange(0, 1)
    WIND_SPEED = random.randrange(3, 25)
    WIND_ANGLE = random.randrange(-70, 310)
    RATE_OF_TURN = random.randrange(-1, 1)
    SIGNIFICANT_WAVE_HEIGHT = random.randrange(1, 2)
    WAVE_HEIGHT = random.randrange(3, 4)
    return (NORTHWARD_CURRENT, EASTWARD_CURRENT, WIND_RELATIVE_DIRECTION, WIND_RELATIVE_SPEED, 
            AIR_TEMPERATURE_AT_10M, TRANSVERSE_GROUND_SPEED, AIR_PRESSURE_AT_SEA_LEVEL, WIND_SPEED, 
            WIND_ANGLE, RATE_OF_TURN, WAVE_DIRECTION, SWELL_WAVE_DIRECTION, 
            SIGNIFICANT_WAVE_HEIGHT, WAVE_HEIGHT)

#this function combines all of the above and creates a nested list with data for prediction for each day (which equals to duration)
def create_data_for_pred(duration, rpm, aft_draft, fore_draft, heading):
    list_for_predict = []
    i=1
    while i<= duration:
        dummy_list=[]
        for j in range(5):
            dummy_list.append(create_var_dummy()[j])
        dummy_list.append(fore_draft)
        dummy_list.append(heading)
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[0])
        dummy_list.append(create_var_dummy()[5])
        dummy_list.append(aft_draft)
        dummy_list.append(rpm)
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[1])
        dummy_list.append(create_var_dummy()[6])
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[2])
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[3])
        dummy_list.append(create_var_dummy()[7])
        dummy_list.append(create_var_dummy()[8])
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[4])
        for k in range(8):
            dummy_list.append(create_random_env_vars()[k])
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[5])
        dummy_list.append(create_random_env_vars()[8])
        dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[6])
        for l in range(9,14):
            dummy_list.append(create_random_env_vars()[l])
        list_for_predict.append(dummy_list)
        i+=1
    return (list_for_predict)
#create_data_for_pred(10, 40, 11.33, 9.51, 161.33)

#Creating a list of labels to be used in chart
def create_labels(duration):
    list_of_labels = [str(n) for n in range(1, int(duration)+1)]
    list_of_labels = [f"Fuel cons for day: {x}" for x in list_of_labels]
    return list_of_labels