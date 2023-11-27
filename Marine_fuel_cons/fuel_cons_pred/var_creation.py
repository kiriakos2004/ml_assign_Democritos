import random

def create_var_inherited(rpm, aft_draft, fore_draft, heading):
    LIST = 0
    MIDDLE_DRAFT_P = (aft_draft + fore_draft)/2
    MIDDLE_DRAFT_S = (aft_draft + fore_draft)/2
    TRIM = aft_draft - fore_draft
    COURSE_OVER_GROUND = heading
    if (0<rpm and 10<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    elif (10<rpm and 20<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    elif (20<rpm and 30<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    elif (30<rpm and 40<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    elif (40<rpm and 50<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    elif (50<rpm and 60<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    elif (60<rpm and 70<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    elif (70<rpm and 80<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    elif (80<rpm and 90<=rpm):
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    else:                   
        FUEL_OIL_FLOW_RETURN = 0
        FUEL_OIL_FLOW_SUPPLY = 0
        LONGITUDINAL_GROUND_SPEED = 0
        LONGITUDINAL_WATER_SPEED = 0
        TURBOCHARGER_SPEED = 0
        SHAFT_POWER = 0
        PROPELLER_SHAFT_THRUST = 0
        PROPELLER_SHAFT_TORQUE = 0
        SPEED_OVER_GROUND = 0
        SPEED_THROUGH_WATER = 0
    return ()
create_var_inherited(40, 8, 8, 160)

def create_var_dummy():
    FUEL_OIL_SUPPLY_TEMPERATURE = 100.22
    FUEL_OIL_RETURN_TEMPERATURE = 99.94
    INTERMEDIATE_SHAFT_BEARING_TEMP = 33.36
    MAIN_ENGINE_SCAVENGE_AIR_PRESSURE = 5.48
    PROPELLER_SHAFT_REVOLUTIONS = 805.99
    ME_AXIAL_VIBRATION = 0.67
    FUEL_OIL_INLET_PRESSURE = 1.0
    FUEL_OIL_INLET_TEMPERATURE = 100.46
    TURBOCHARGER_EXH_EXH_GAS_INLET_TEMP = 228.47
    TURBOCHARGER_EXH_EXH_GAS_OUTLET_TEMP = 171.61
    THRUST_BEARING_TEMPERATURE = 48.1
    RATE_OF_TURN = 0.03
    STARBOARD_RUDDER_SENSOR = 0
    STERN_TUBE_BEARING_TEMPERATURE = 28.54
    THRUST_MAIN_BEARING_TEMP = 43.62
    TRANSVERSE_GROUND_SPEED = 0.25
    WATER_DEPTH = 81.91
    return (FUEL_OIL_SUPPLY_TEMPERATURE,FUEL_OIL_RETURN_TEMPERATURE, INTERMEDIATE_SHAFT_BEARING_TEMP, MAIN_ENGINE_SCAVENGE_AIR_PRESSURE,
            PROPELLER_SHAFT_REVOLUTIONS, ME_AXIAL_VIBRATION, FUEL_OIL_INLET_PRESSURE, FUEL_OIL_INLET_TEMPERATURE, TURBOCHARGER_EXH_EXH_GAS_INLET_TEMP,
            TURBOCHARGER_EXH_EXH_GAS_OUTLET_TEMP, THRUST_BEARING_TEMPERATURE, RATE_OF_TURN, STARBOARD_RUDDER_SENSOR, STERN_TUBE_BEARING_TEMPERATURE,
            THRUST_MAIN_BEARING_TEMP, TRANSVERSE_GROUND_SPEED, WATER_DEPTH)
create_var_dummy()

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
#create_random_env_vars()

#this function combines all of the above and creates a nested list with data for prediction for each day (which equals to duration)
def create_data_for_pred(duration):
    list_for_predict = []
    i=1
    while i<= duration:
        dummy_list=[]
        for j in range(22):
            dummy_list.append(create_random_env_vars()[j])
        for z in range(3):
            dummy_list.append(z)
        list_for_predict.append(dummy_list)
        i+=1
    print(list_for_predict)
    return (list_for_predict)
create_data_for_pred(2)