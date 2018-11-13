#!/usr/bin/env python3
"""
A container for LightSensors which provides a fixed physical frame for the
LightSensors on be attached to so that moving the SensorMount affects all
attached LightSensors appropriately.

SensorMounts allow translations and rotations when specifying a move. Thus
they do not allow for six degrees of freedom of movement. This is sufficient
for modeling the movements of a cart, but would not be good enough for a
flying drone.
"""

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
        self.location = {'x':0, 'y':0, 'z':0}
        self.rotation = 0

    def add_new_sensor(self, sensor):
        """
        Attach a new sensor object to the SensorMount
        """
        self.sensor_list.append(sensor)

    def move_to_position(self, location, pitch):
        """
        Move this SensorMount as well as all the attached sensors to
        the new location defined by the provided translation and rotation
        """
        pass

    def current_position(self):
        """
        Query for the current position of the SensorMount
        """
        return self.location
