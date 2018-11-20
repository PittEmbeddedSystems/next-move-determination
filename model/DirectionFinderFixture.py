#!/usr/bin/env python3
"""
Software fixture for the DirectionFinder object to evaluate how effective its
strategy is at moving to the area of the highest light
"""
import math

from LightSource import LightSource
from LightSensor import LightSensor
from SensorMount import SensorMount

import sys
sys.path.append("..")
from DirectionFinder import DirectionFinder

def run_model():
    # Put a light-bulb 10 feet high in the center of the room
    light_source_location = (0, 0, 304)
    light_source_intensity_lux = 500
    source = LightSource(light_source_location, light_source_intensity_lux)

    # Initialize Sensors centered around the center of the room in the pattern
    # we want our array to use
    sensor_array = []
    sensor_input_range = (0, 304)
    sensor_output_range = (0, 1023)
    sensor_array.append(LightSensor((0, 30, 10),  \
        sensor_input_range, sensor_output_range))

    sensor_array.append(LightSensor((30 * math.sqrt(2)/2, \
        30 * math.sqrt(2)/2, 10),  sensor_input_range, \
        sensor_output_range))

    sensor_array.append(LightSensor((30, 0, 10), \
        sensor_input_range, sensor_output_range))

    sensor_array.append(LightSensor((30 * math.sqrt(2)/2, \
        -30 * math.sqrt(2)/2, 10), \
         sensor_input_range, sensor_output_range))

    sensor_array.append(LightSensor((0, -30, 10), \
        sensor_input_range, sensor_output_range))

    sensor_array.append(LightSensor((-30 * math.sqrt(2)/2, \
        -30 * math.sqrt(2)/2, 10), \
        sensor_input_range, sensor_output_range))

    sensor_array.append(LightSensor((-30, 0, 10), \
        sensor_input_range, sensor_output_range))

    sensor_array.append(LightSensor((-30 * math.sqrt(2)/2, \
        30 * math.sqrt(2)/2, 10), \
        sensor_input_range, sensor_output_range))

    # Initialize our sensor mount and attach all our sensors
    cart = SensorMount()
    for sensor in sensor_array:
        cart.add_new_sensor(sensor)

    # Move the mount to somewhere away from just below the light
    cart.move_to_position((0, -100, 0), 0)


    #Initialize DirectionFinder to be evaluated
    direction_finder = DirectionFinder()

    # Keep iterating on getting the next direction and moving until we either
    # stabilize or we have tried more than the maximum specified times
    for iteration in range(0, 100):
        # Get all the sensor location and outputs to feed into the DF
        current_sensor_data = []
        cart_location = cart.current_position()

        for sensor_index in range(0, 7):
            current_sensor = cart.get_sensor(sensor_index)
            global_sensor_location = current_sensor.current_position()

            incident_light = source.get_intensity_at_location(global_sensor_location)
            measured_light = current_sensor.output_from_sources(incident_light)
            relative_sensor_location =  (global_sensor_location[0] - cart_location[0], \
                global_sensor_location[1] - cart_location[1])
            print(str(sensor_index) + ": relative sensor location " + str(relative_sensor_location))
            print("   Sensor location: " + str(global_sensor_location))
            sensor_element = { 'amp':measured_light, 'location': relative_sensor_location }
            current_sensor_data.append(sensor_element)

        next_move = direction_finder.FindDirection(current_sensor_data)
        print("Next Move: " + str(next_move))

        # Figure out rotation and translation
        next_translation = ( cart_location[0] + next_move[0], \
            cart_location[1] + next_move[1], 10)
        next_rotation = 0
        cart.move_to_position(next_translation, next_rotation)

        print(str(iteration) + ": Cart Location: " + str(cart.current_position()))
        if cart.current_position() == (0, 0, 10):
            print("Reached ideal spot in " + str(iteration) + " iterations")
            return


if __name__ == "__main__":
    run_model()