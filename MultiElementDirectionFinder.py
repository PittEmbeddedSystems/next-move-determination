#!/usr/bin/env python3
"""
Implementation of a Direction Finding algorithm which uses multiple elements'
measurements to determine Angle-Of-Arrival (AOA)
"""

from operator import itemgetter

from DirectionFinder import DirectionFinder

class MultiElementDirectionFinder(DirectionFinder):
    """
    This class estimates the AOA of a signal based on the
    measured amplitudes of an array of circularly disposed elements.

    This approach will allow for better resolution DF than single element DF
    because it essentially interpolates between sensors.
    """

    def __init__(self, num_elements):
        """
        Initialize a MultiElementDirectionFinder for num_element elements
        """
        self.num_elements = num_elements

    def FindDirection(self, sensor_data):
        """
        This method accepts an array of sensor data which includes individual
        array locations as well as amplitude measurements. It responds with a
        vector representing the estimated AOA. If an AOA cannot be determined
        from this set of data, this method will return an empty vector ()
        """

        # Find the N elements with the highest amplitudes
        highest_elements = self._find_highest_elements(sensor_data, self.num_elements)

        # Add the vectors together and return the resultant vector

        resultant_vector = [ 0, 0 ]
        for element in highest_elements:
            resultant_vector[0] = resultant_vector[0] + element['location'][0]
            resultant_vector[1] = resultant_vector[1] + element['location'][1]

        return resultant_vector


    def _find_highest_elements(self, sensor_data, num_elements):
        """
        Utility method to identify and return the num_elements of sensor data
        with the highest amplitudes.
        """

        sorted_data = sorted(sensor_data, key=itemgetter('amp'), reverse=True)

        highest_elements = [sorted_data[i] for i in range(0, num_elements)]

        return highest_elements
