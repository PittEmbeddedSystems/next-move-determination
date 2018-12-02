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
    cart.move_to_position((60, 0, 0), 0)


    #Initialize DirectionFinder to be evaluated
    direction_finder = DirectionFinder()

    # Keep iterating on getting the next direction and moving until we either
    # stabilize or we have tried more than the maximum specified times
    for iteration in range(1, 25):
        # Get all the sensor location and outputs to feed into the DF
        current_sensor_data = []
        cart_location = cart.current_position()
        print(str(iteration) + ": Cart Location: " + str(cart_location))

        for sensor_index in range(0, 7):
            current_sensor = cart.get_sensor(sensor_index)
            global_sensor_location = current_sensor.current_position()

            incident_light = source.get_intensity_at_location(global_sensor_location)
            measured_light = current_sensor.output_from_sources(incident_light)
            relative_sensor_location =  (global_sensor_location[0] - cart_location[0], \
                global_sensor_location[1] - cart_location[1], \
                cart_location[2])
            sensor_element = { 'amp':measured_light, 'location':relative_sensor_location }
            current_sensor_data.append(sensor_element)

        next_move = direction_finder.FindDirection(current_sensor_data)
        print("Next Move: {} ".format(next_move))
        current_sensor_data.clear()

        # We only want to move 5 cm in that direction, so figure out that point
        move_vector = [next_move[0] - cart_location[0], next_move[1]  - cart_location[1]]
        orig_magnitude = math.sqrt(math.pow(move_vector[0], 2) + math.pow(move_vector[1], 2))
        scaled_move = [0, 0]
        if orig_magnitude != 0.0:
            scaled_move = [ 5 * ( move_vector[0]) / orig_magnitude, 5 * (move_vector[1]) / orig_magnitude ]

        print("Scaled Move: {}".format(scaled_move))

        # Calculate the translation the move represents
        next_translation = ( cart_location[0] + scaled_move[0], \
            cart_location[1] + scaled_move[1], \
            0)


        # The SensorMount doesn't have a defined front so by convention we'll
        # say that the first sensor attached to it represents the front.
        current_cart_front = cart.get_sensor(0).current_position()
        current_cart_angle = math.atan2(current_cart_front[1], current_cart_front[2])
        final_cart_angle = math.atan2(next_move[1], next_move[0])
        next_rotation = round(final_cart_angle - current_cart_angle, 2)

        cart.move_to_position(next_translation, next_rotation)

        if scaled_move == [0, 0]:
            print("Reached ideal spot in " + str(iteration) + " iterations")
            return

        print("   Current Error: " + str(math.sqrt(math.pow(next_translation[0], 2) \
            + math.pow(next_translation[1], 2))))


if __name__ == "__main__":
    run_model()