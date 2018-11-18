#!/usr/bin/env python3
"""
Unit tests for the LightSource object
"""

import sys
import unittest
sys.path.append("..")
from LightSource import LightSource

class LightSourceTests(unittest.TestCase):
    """
    Tests for the proper operation of the LightSource object
    """
    def testLocationInitialization(self):
        """
        Make sure that a LightSource initialized at a given location reports
        that as its location.
        """
        initial_location = (200, 300, 700)
        intensity = 505
        source_under_test = LightSource(initial_location, intensity)

        self.assertEqual(source_under_test.get_location(), initial_location)

    def testIntensityInitialization(self):
        """
        Make sure that a LightSource object initialized with a given intensity
        reports that as its output intensity.
        """
        initial_location = (200, 300, 700)
        intensity = 505
        source_under_test = LightSource(initial_location, intensity)

        self.assertEqual(source_under_test.get_output_intensity(), intensity)

    def testIntensityAtOneMeter(self):
        """
        Make sure that a LigthSource object transmits its intensity accurately
        to a sensor 1 meter away.
        """
        initial_location = (200, 300, 700)
        intensity = 505
        source_under_test = LightSource(initial_location, intensity)

        # Assuming that units of intensity are in Lux and distance is in cm
        # then the resultant light intensity should be determined by the
        # equation: Resultant = Output / (4 * pi * 1^2)
        expected_resultant = 40.1866231307
        sensor_location = (300, 300, 700)
        recorded_intensity = source_under_test.get_intensity_at_location(sensor_location)
        self.assertAlmostEqual(recorded_intensity, expected_resultant, 6)

    def testIntensityAtTwoMeters(self):
        """
        Make sure that a LigthSource object transmits its intensity accurately
        to a sensor 1 meter away.
        """
        initial_location = (200, 300, 700)
        intensity = 505
        source_under_test = LightSource(initial_location, intensity)

        # Assuming that units of intensity are in Lux and distance is in cm
        # then the resultant light intensity should be determined by the
        # equation: Resultant = Output / (4 * pi * 2^2)
        expected_resultant = 10.0466557827
        sensor_location = (400, 300, 700)
        recorded_intensity = source_under_test.get_intensity_at_location(sensor_location)
        self.assertAlmostEqual(recorded_intensity, expected_resultant, 6)

if __name__ == "__main__":
    unittest.main()
