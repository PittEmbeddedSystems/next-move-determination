#!/usr/bin/env python3
"""
Contains unit tests for the LightSensor object
"""
import sys
import unittest
sys.path.append("..")
from LightSensor import LightSensor

class LightSensorTests(unittest.TestCase):
    """
    Suite of test cases to confirm the expected operation of the LightSensor
    object
    """

    def testInitializePosition(self):
        """
        Confirm that the LightSensor initializes the position of the object
        based on the provided coordinates.
        """
        initial_location = (1, 5, 3)
        initial_input_range = (1, 5)
        initial_output_range = (1, 5)
        sensor_under_test = LightSensor(initial_location, initial_input_range, \
        initial_output_range)
        self.assertEqual(sensor_under_test.current_position(), initial_location)

    def testMovePosition(self):
        """
        Confirm that when a LightSensor is moved after creation that the object
        reports the updated location rather than the initial one.
        """
        initial_location = (1, 5, 3)
        initial_input_range = (1, 5)
        initial_output_range = (1, 5)

        new_location = (2, 3, 2)
        sensor_under_test = LightSensor(initial_location, initial_input_range, \
        initial_output_range)
        sensor_under_test.move_to_position(new_location)
        self.assertEqual(sensor_under_test.current_position(), new_location)

    def testIdenticalTranslation(self):
        """
        Confirm the trivial case that when a light sensors input range and
        output range are identical that it returns an output that matches the
        provided input.
        """
        initial_location = (1, 5, 3)
        initial_input_range = (1, 5)
        initial_output_range = (1, 5)
        sensor_under_test = LightSensor(initial_location, initial_input_range, \
        initial_output_range)

        incident_light = 4
        self.assertEqual(sensor_under_test.output_from_sources(incident_light), \
        incident_light)

    def testShiftTranslation(self):
        """
        Confirm the case that when the output range reflects an offset from the
        input range that the LightSensor will return a shifted output relative
        to the provided input
        """
        initial_location = (1, 5, 3)
        initial_input_range = (1, 5)
        initial_output_range = (2, 6)
        sensor_under_test = LightSensor(initial_location, initial_input_range, \
        initial_output_range)

        incident_light = 4
        expected_output_light = 5
        self.assertEqual(sensor_under_test.output_from_sources(incident_light), \
        expected_output_light)

    def testScaledTranslation(self):
        """
        Confirm the common case that when the output range represents a shift
        and a scaling of the input, the LightSensor will return a properly
        translated output for a given input.
        """
        initial_location = (1, 5, 3)
        initial_input_range = (1, 5)
        initial_output_range = (2, 10)
        sensor_under_test = LightSensor(initial_location, initial_input_range, \
        initial_output_range)

        incident_light = 4
        expected_output_light = 8
        self.assertEqual(sensor_under_test.output_from_sources(incident_light), \
        expected_output_light)

if __name__ == "__main__":
    unittest.main()
