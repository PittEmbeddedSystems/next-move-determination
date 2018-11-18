#!/usr/bin/env python3
"""
Contains the implementation of a LightSource within the model
"""

import math

class LightSource(object):
    """
    Object representing an omni-directional light source at a specified location
    and of a specified intensity. This location of this LightSource is not
    changed once initialized.
    """

    def __init__(self, location, intensity):
        """
        Initialize a LightSource at a specified location and intensity
        """
        self.location = location
        self.output_intensity = intensity

    def get_location(self):
        """
        Queries the location of the LightSource
        """
        return self.location

    def get_output_intensity(self):
        """
        Queries the output intensity of the light source
        """
        return self.output_intensity

    def get_intensity_at_location(self, location):
        """
        Queries the inicident intensity of the light source at a specified
        location
        """

        # Convert coordinates to m from cm and calculate distance
        distance_sq = math.pow((self.location[0] - location[0]) / 100, 2) \
            + math.pow((self.location[1] - location[1]) / 100, 2) \
            + math.pow((self.location[2] - location[2]) / 100, 2)

        return self.output_intensity / (4 * math.pi * distance_sq)
