#!/usr/bin/env python3

import sys
import unittest
sys.path.append("..")
from LightSensor import LightSensor

class LightSensorTests(unittest.TestCase):

    def testInitializePosition(self):
        initial_location = (1, 5, 3)
        initial_input_range = (1, 5)
        initial_output_range = (1, 5)
        sensor_under_test = LightSensor(initial_location, initial_input_range, \
        initial_output_range)
        self.assertEqual(sensor_under_test.current_position(), initial_location)

    def testMovePosition(self):
        initial_location = (1, 5, 3)
        initial_input_range = (1, 5)
        initial_output_range = (1, 5)

        new_location = (2, 3, 2)
        sensor_under_test = LightSensor(initial_location, initial_input_range, \
        initial_output_range)
        sensor_under_test.move_to_position(new_location)
        self.assertEqual(sensor_under_test.current_position(), new_location)

    def testIdenticalTranslation(self):
        initial_location = (1, 5, 3)
        initial_input_range = (1, 5)
        initial_output_range = (1, 5)
        sensor_under_test = LightSensor(initial_location, initial_input_range, \
        initial_output_range)

        incident_light = 4
        self.assertEqual(sensor_under_test.output_from_sources(incident_light), \
        incident_light)

    def testShiftTranslation(self):
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
