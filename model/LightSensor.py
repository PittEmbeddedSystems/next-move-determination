#!/usr/bin/env python3
"""
Provides a simple representation of a light sensor which can be used to
model a single light sensitive element and associated A/D
"""

class LightSensor(object):
    """
    Each LightSensor represents a photosensitive element at a specific
    location which translates the incident light received from any light
    sensors in the environment into an integer.
    """
    def __init__(self, location, input_range, output_range):
        """
        A light sensor is defined by a location defined by its x, y, and z
        coordinates. It also must define the range of inputs and outputs
        that it can translate.
        """
        self.move_to_position(location)
        self.input_range = input_range
        self.output_range = output_range

    def move_to_position(self, location):
        """
        Move a light sensors global position to that specified by the
        provided coordinates.
        """
        self.location = location

    def current_position(self):
        """
        Query the current location of the LightSensor
        """
        return (self.location.x, self.location.y, self.location.z)

    def output_from_sources(self, incident_light):
        """
        Determine an output based on the specified input
        """
        return incident_light * (self.output_range) / (self.input_range)
