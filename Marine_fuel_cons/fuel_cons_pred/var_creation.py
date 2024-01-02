import random
from . import dict

#Creating variables based of the input from the user (these variables in a real aplication will be replaced by the ship's ADLM system)
def create_var_inherited(rpm, aft_draft, fore_draft, heading):   
    LIST = 0
    MIDDLE_DRAFT_P = (aft_draft + fore_draft)/2
    MIDDLE_DRAFT_S = (aft_draft + fore_draft)/2
    COURSE_OVER_GROUND = heading
    RATE_OF_TURN = 0
    STARBOARD_RUDDER_SENSOR = 0
    WATER_DEPTH = 80
    if 0 <= rpm < 10:
        FUEL_OIL_FLOW_RETURN = 2600
        FUEL_OIL_FLOW_SUPPLY = 2700
        TURBOCHARGER_SPEED = 850
        SHAFT_POWER = 180
        PROPELLER_SHAFT_THRUST = -60
        PROPELLER_SHAFT_TORQUE = 80
        SPEED_OVER_GROUND = 2
        SPEED_THROUGH_WATER = 2
    elif 10 <= rpm < 20:
        FUEL_OIL_FLOW_RETURN = 3600
        FUEL_OIL_FLOW_SUPPLY = 3800
        TURBOCHARGER_SPEED = 1300
        SHAFT_POWER = 500
        PROPELLER_SHAFT_THRUST = -100
        PROPELLER_SHAFT_TORQUE = 120
        SPEED_OVER_GROUND = 4
        SPEED_THROUGH_WATER = 4
    elif 20 <= rpm < 30:
        FUEL_OIL_FLOW_RETURN = 3300
        FUEL_OIL_FLOW_SUPPLY = 3500
        TURBOCHARGER_SPEED = 2600
        SHAFT_POWER = 900
        PROPELLER_SHAFT_THRUST = -130
        PROPELLER_SHAFT_TORQUE = 220
        SPEED_OVER_GROUND = 6
        SPEED_THROUGH_WATER = 6
    elif 30 <= rpm < 40:
        FUEL_OIL_FLOW_RETURN = 3500
        FUEL_OIL_FLOW_SUPPLY = 3800
        TURBOCHARGER_SPEED = 3100
        SHAFT_POWER = 1100
        PROPELLER_SHAFT_THRUST = -160
        PROPELLER_SHAFT_TORQUE = 260
        SPEED_OVER_GROUND = 8
        SPEED_THROUGH_WATER = 8
    elif 40 <= rpm < 50:
        FUEL_OIL_FLOW_RETURN = 3600
        FUEL_OIL_FLOW_SUPPLY = 4000
        TURBOCHARGER_SPEED = 4500
        SHAFT_POWER = 1600
        PROPELLER_SHAFT_THRUST = -200
        PROPELLER_SHAFT_TORQUE = 340
        SPEED_OVER_GROUND = 9.5
        SPEED_THROUGH_WATER = 9.5
    elif 50 <= rpm < 60:
        FUEL_OIL_FLOW_RETURN = 2800
        FUEL_OIL_FLOW_SUPPLY = 3500
        TURBOCHARGER_SPEED = 6200
        SHAFT_POWER = 2900
        PROPELLER_SHAFT_THRUST = -350
        PROPELLER_SHAFT_TORQUE = 500
        SPEED_OVER_GROUND = 11
        SPEED_THROUGH_WATER = 11
    elif 60 <= rpm < 70:
        FUEL_OIL_FLOW_RETURN = 2500
        FUEL_OIL_FLOW_SUPPLY = 3200
        TURBOCHARGER_SPEED = 9500
        SHAFT_POWER = 4500
        PROPELLER_SHAFT_THRUST = -500
        PROPELLER_SHAFT_TORQUE = 650
        SPEED_OVER_GROUND = 13
        SPEED_THROUGH_WATER = 13
    elif 70 <= rpm < 80:
        FUEL_OIL_FLOW_RETURN = 3500
        FUEL_OIL_FLOW_SUPPLY = 4600
        TURBOCHARGER_SPEED = 11000
        SHAFT_POWER = 6000
        PROPELLER_SHAFT_THRUST = -600
        PROPELLER_SHAFT_TORQUE = 750
        SPEED_OVER_GROUND = 13.5
        SPEED_THROUGH_WATER = 13.5
    elif 80 <= rpm < 90:
        FUEL_OIL_FLOW_RETURN = 2100
        FUEL_OIL_FLOW_SUPPLY = 3700
        TURBOCHARGER_SPEED = 13500
        SHAFT_POWER = 8000
        PROPELLER_SHAFT_THRUST = -650
        PROPELLER_SHAFT_TORQUE = 860
        SPEED_OVER_GROUND = 15
        SPEED_THROUGH_WATER = 15
    else:
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    return (LIST, MIDDLE_DRAFT_P, MIDDLE_DRAFT_S, COURSE_OVER_GROUND, RATE_OF_TURN, STARBOARD_RUDDER_SENSOR,
            WATER_DEPTH, FUEL_OIL_FLOW_RETURN, FUEL_OIL_FLOW_SUPPLY, TURBOCHARGER_SPEED, SHAFT_POWER,
            PROPELLER_SHAFT_THRUST, PROPELLER_SHAFT_TORQUE, SPEED_OVER_GROUND, SPEED_THROUGH_WATER)


#Creating dummy variables from the mean value of the training dataset
def create_var_dummy():
    FUEL_OIL_SUPPLY_TEMPERATURE = dict.dict_of_attributes['FUEL OIL SUPPLY TEMPERATURE'][0]
    FUEL_OIL_RETURN_TEMPERATURE = dict.dict_of_attributes['FUEL OIL RETURN TEMPERATURE'][0]
    INTERMEDIATE_SHAFT_BEARING_TEMP = dict.dict_of_attributes['INTERMEDIATE SHAFT BEARING TEMP'][0]
    MAIN_ENGINE_SCAVENGE_AIR_PRESSURE = dict.dict_of_attributes['MAIN ENGINE SCAVENGE AIR PRESSURE'][0]
    ME_AXIAL_VIBRATION = dict.dict_of_attributes['ME AXIAL VIBRATION'][0]
    FUEL_OIL_INLET_PRESSURE = dict.dict_of_attributes['FUEL OIL INLET PRESSURE'][0]
    FUEL_OIL_INLET_TEMPERATURE = dict.dict_of_attributes['FUEL OIL INLET TEMPERATURE'][0]
    TURBOCHARGER_EXH_EXH_GAS_INLET_TEMP = dict.dict_of_attributes['TURBOCHARGER EXH EXH GAS INLET TEMP'][0]
    TURBOCHARGER_EXH_EXH_GAS_OUTLET_TEMP = dict.dict_of_attributes['TURBOCHARGER EXH EXH GAS OUTLET TEMP'][0]
    THRUST_BEARING_TEMPERATURE = dict.dict_of_attributes['THRUST BEARING TEMPERATURE'][0]
    STERN_TUBE_BEARING_TEMPERATURE = dict.dict_of_attributes['STERN TUBE BEARING TEMPERATURE'][0]
    THRUST_MAIN_BEARING_TEMP = dict.dict_of_attributes['THRUST MAIN BEARING TEMP'][0]
    TRANSVERSE_GROUND_SPEED = dict.dict_of_attributes['TRANSVERSE GROUND SPEED'][0]
    return (FUEL_OIL_SUPPLY_TEMPERATURE,FUEL_OIL_RETURN_TEMPERATURE, INTERMEDIATE_SHAFT_BEARING_TEMP, MAIN_ENGINE_SCAVENGE_AIR_PRESSURE,
            ME_AXIAL_VIBRATION, FUEL_OIL_INLET_PRESSURE, FUEL_OIL_INLET_TEMPERATURE, TURBOCHARGER_EXH_EXH_GAS_INLET_TEMP,
            TURBOCHARGER_EXH_EXH_GAS_OUTLET_TEMP, THRUST_BEARING_TEMPERATURE, STERN_TUBE_BEARING_TEMPERATURE,
            THRUST_MAIN_BEARING_TEMP, TRANSVERSE_GROUND_SPEED)


#Creating dummy enviromental variables in order to show the flustration in ship's fuel consuption. (These variables in a real application will be consumed by a weather API)
def create_random_env_vars():
    WIND_ANGLE = random.randrange(-293, -51)
    WIND_SPEED = random.randrange(3, 22)
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
    return (WIND_ANGLE, WIND_SPEED, AIR_PRESSURE_AT_SEA_LEVEL, AIR_TEMPERATURE_AT_10M, CURRENT_DIRECTION,
            CURRENT_SPEED, EASTWARD_CURRENT, WAVE_HEIGHT, WAVE_DIRECTION, WAVE_LENGTH, NORTHWARD_CURRENT,
            SEA_TEMPERATURE, SIGNIFICANT_WAVE_HEIGHT, SWELL_WAVE_HEIGHT, SWELL_WAVE_DIRECTION, SWELL_WAVE_LENGTH,
            SWELL_SIGNIFICANT_WAVE_HEIGHT, WIND_RELATIVE_DIRECTION, WIND_RELATIVE_SPEED, WINDWAVE_WAVE_HEIGHT,
            WINDWAVE_WAVE_DIRECTION, WINDWAVE_WAVE_LENGTH, WINDWAVE_WAVE_HEIGHT_1)


#this function combines all of the above and creates a nested list with data for prediction for each day (which equals to duration)
def create_data_for_pred(duration, rpm, aft_draft, fore_draft, heading):
    list_for_predict = []
    i=1
    while i<= duration:
        dummy_list=[]
        dummy_list.append(rpm)
        for j in range(15):
            dummy_list.append(create_var_inherited(rpm, aft_draft, fore_draft, heading)[j])
        for k in range(13):
            dummy_list.append(create_var_dummy()[k])
        for l in range(23):
            dummy_list.append(create_random_env_vars()[l])    
        list_for_predict.append(dummy_list)
        i+=1
    return (list_for_predict)
create_data_for_pred(10, 40, 11.33, 9.51, 161.33)

#Creating a list of labels to be used in chart
def create_labels(duration):
    list_of_labels = [str(n) for n in range(1, int(duration)+1)]
    list_of_labels = [f"Fuel cons for day: {x}" for x in list_of_labels]
    return list_of_labels