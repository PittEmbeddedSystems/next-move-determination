#!/usr/bin/env python3
"""
A container for LightSensors which provides a fixed physical frame for the
LightSensors attached to it so that moving the SensorMount affects all
attached LightSensors appropriately.

SensorMounts allow translations and rotations when specifying a move. Thus
they do not allow for six degrees of freedom of movement. This is sufficient
for modeling the movements of a cart, but would not be good enough for a
flying drone.
"""

import math

class SensorMount(object):
    """
    Represent an apparatus on which sensors may be mounted such that as
    the SensorMount is moved, the attached sensors are also moved.
    """
    def __init__(self):
        """
        Initialize a SensorMount object at the origin with no attached sensors
        """
        self.sensor_list = []
        self.location = (0, 0, 0)
        self.rotation = 0

    def add_new_sensor(self, sensor):
        """
        Attach a new sensor object to the SensorMount
        """
        self.sensor_list.append(sensor)

    def move_to_position(self, location, rotation):
        """
        Move this SensorMount as well as all the attached sensors to
        the new location defined by the provided translation and rotation
        """
        rotation_rads = math.radians(rotation)

        for index, sensor in enumerate(self.sensor_list):
            current_position = sensor.current_position()
            relative_x = current_position[0] - self.location[0]
            relative_y = current_position[1] - self.location[1]
            relative_z = current_position[2] - self.location[2]
            # The rotation is calculated about the mount position
            rotated_x = relative_x * math.cos(rotation_rads) \
                + relative_y * math.sin(rotation_rads)

            rotated_y = - relative_x * math.sin(rotation_rads) \
                + relative_y * math.cos(rotation_rads)

            # ASSUMPITION: Our mount operates on a flat plane
            rotated_z = relative_z

            # Translate back to absolute coordinates
            rotated_position = (rotated_x + self.location[0], \
                rotated_y + self.location[1], \
                    rotated_z + self.location[2] )

            # The translation is the difference in the coordinates between
            # the initial and final position.
            new_x = rotated_position[0] \
                + (location[0] - self.location[0])
            new_y = rotated_position[1] \
                + (location[1] - self.location[1])
            new_z = rotated_position[2] \
                + (location[2] - self.location[2])

            new_sensor_position = (new_x, new_y, new_z)
            sensor.move_to_position(new_sensor_position)
            self.sensor_list[index] = sensor

        self.location = location
    
    def get_sensor(self, sensor_index):
        return self.sensor_list[sensor_index]
    

    def current_position(self):
        """
        Query for the current position of the SensorMount
        """
        return self.location
