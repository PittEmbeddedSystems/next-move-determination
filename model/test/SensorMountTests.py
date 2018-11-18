#!/usr/bin/env python3
"""
Contains unit tests for SensorMount object
"""
import sys
import unittest
sys.path.append("..")
from LightSensor import LightSensor
from SensorMount import SensorMount

class SensorMountTests(unittest.TestCase):
    """
    SensorMount unit test fixture
    """
    def testSimpleTranslation(self):
        """
        Confirm that a SensorMount correctly reports its own position
        """
        mount_under_test = SensorMount()

        mount_location = (1, 2, 3)
        mount_under_test.move_to_position(mount_location, 0)
        self.assertEqual(mount_under_test.current_position(), mount_location)

    def testSimpleTranslationWithSensor(self):
        """
        Confirm that a SensorMount with a single sensor properly translates its
        Sensor object's location when it is moved without a rotation
        """
        mount_under_test = SensorMount()

        sensor_location = (1, 0, 0)
        attached_sensor = LightSensor(sensor_location, (), ())

        mount_location = (1, 2, 3)
        mount_under_test.add_new_sensor(attached_sensor)
        mount_under_test.move_to_position(mount_location, 0)
        self.assertEqual(mount_under_test.get_sensor(0).current_position(), (2, 2, 3))

    def test90DegreRotation(self):
        """
        Confirm that a SensorMount with a single sensor properly rotates its
        Sensor object's location when it is rotated 90 degrees without a
        translation.
        """
        mount_under_test = SensorMount()

        sensor_location = (1, 0, 0)
        attached_sensor = LightSensor(sensor_location, (), ())

        mount_location = (0, 0, 0)
        rotated_location = (0, -1, 0)
        mount_under_test.add_new_sensor(attached_sensor)
        mount_under_test.move_to_position(mount_location, 90)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[0],\
            rotated_location[0], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[1],\
            rotated_location[1], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[2],\
            rotated_location[2], 6)

    def test180DegreeRotation(self):
        """
        Confirm that a SensorMount with a single sensor properly rotates its
        Sensor object's location when it is rotated 180 degrees without a
        translation.
        """
        mount_under_test = SensorMount()

        sensor_location = (1, 0, 0)
        attached_sensor = LightSensor(sensor_location, (), ())

        mount_location = (0, 0, 0)
        rotated_location = (-1, 0, 0)
        mount_under_test.add_new_sensor(attached_sensor)
        mount_under_test.move_to_position(mount_location, 180)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[0],\
            rotated_location[0], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[1],\
            rotated_location[1], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[2],\
            rotated_location[2], 6)

    def test270DegreeRotation(self):
        """
        Confirm that a SensorMount with a single sensor properly rotates its
        Sensor object's location when it is rotated 270 degrees without a
        translation.
        """
        mount_under_test = SensorMount()

        sensor_location = (1, 0, 0)
        attached_sensor = LightSensor(sensor_location, (), ())

        mount_location = (0, 0, 0)
        rotated_location = (0, 1, 0)
        mount_under_test.add_new_sensor(attached_sensor)
        mount_under_test.move_to_position(mount_location, 270)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[0],\
            rotated_location[0], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[1],\
            rotated_location[1], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[2],\
            rotated_location[2], 6)

    def test360DegreeRotation(self):
        """
        Confirm that a SensorMount with a single sensor properly rotates its
        Sensor object's location when it is rotated 360 degrees without a
        translation.
        """
        mount_under_test = SensorMount()

        sensor_location = (1, 0, 0)
        attached_sensor = LightSensor(sensor_location, (), ())

        mount_location = (0, 0, 0)
        rotated_location = (1, 0, 0)
        mount_under_test.add_new_sensor(attached_sensor)
        mount_under_test.move_to_position(mount_location, 360)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[0],\
            rotated_location[0], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[1],\
            rotated_location[1], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[2],\
            rotated_location[2], 6)

    def testTranslationAndRotationWithSensor(self):
        """
        Confirm that a SensorMount with a single sensor properly updates its
        Sensor's location when the SensorMount is both rotated and translated.
        """
        mount_under_test = SensorMount()

        sensor_location = (100, 0, 0)
        attached_sensor = LightSensor(sensor_location, (), ())

        mount_location = (2, 5, 7)

        """
        We calculate the expected result manually as
        expected X = (100 * cos(32) + y * sin(32)) + 2
                                rotation             translation
        expected Y = (-100 * sin(32) + y * cos(32)) + 5
                                rotation              translation
        expected Z = z + 7

        Where all trig functions are using degrees,
        x = 100
        y = 0
        z = 0
        """
        resultant_location = (86.804809616, -47.991926423, 7)
        mount_under_test.add_new_sensor(attached_sensor)
        mount_under_test.move_to_position(mount_location, 32)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[0],\
            resultant_location[0], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[1],\
            resultant_location[1], 6)
        self.assertAlmostEqual(mount_under_test.get_sensor(0).current_position()[2],\
            resultant_location[2], 6)

    def testMoveAndRotateMountWithMultipleSensors(self):
        """
        Confirm that a SensorMount with a multiple sensors properly updates its
        Sensor's location when the SensorMount is both rotated and translated.
        """
        mount_under_test = SensorMount()

        attached_sensor = []
        attached_sensor.append(LightSensor((100, 0, 0), (), ()))
        attached_sensor.append(LightSensor((70.710678119, 70.710678119, 0), (), ()))
        attached_sensor.append(LightSensor((0, 100, 0), (), ()))
        attached_sensor.append(LightSensor((-70.710678119, 70.710678119, 0), (), ()))
        attached_sensor.append(LightSensor((-100, 0, 0), (), ()))
        attached_sensor.append(LightSensor((-70.710678119, -70.710678119, 0), (), ()))
        attached_sensor.append(LightSensor((0, -100, 0), (), ()))
        attached_sensor.append(LightSensor((70.710678119, -70.710678119, 0), (), ()))

        mount_location = (2, 5, 7)
        resultant_location = []
        """
        Since we are rotating by 45 degress, each sensor should be rotated to the
        position of the previous one before being translated.
        For example: the second element will end up being rotated to (100, 0, 0)
        then translated by the mount_location (2, 5, 7) to become (102, 5, 7)
        """
        resultant_location.append((72.710678119, -65.710678119, 7))
        resultant_location.append((102, 5, 7))
        resultant_location.append((72.710678119, 75.710678119, 7))
        resultant_location.append((2, 105, 7))
        resultant_location.append((-68.710678119, 75.710678119, 7))
        resultant_location.append((-98, 5, 7))
        resultant_location.append((-68.710678119, -65.710678119, 7))
        resultant_location.append((72.710678119, -65.710678119, 7))

        mount_under_test.add_new_sensor(attached_sensor[0])
        mount_under_test.add_new_sensor(attached_sensor[1])
        mount_under_test.add_new_sensor(attached_sensor[2])
        mount_under_test.add_new_sensor(attached_sensor[3])
        mount_under_test.add_new_sensor(attached_sensor[4])
        mount_under_test.add_new_sensor(attached_sensor[5])
        mount_under_test.add_new_sensor(attached_sensor[6])
        mount_under_test.add_new_sensor(attached_sensor[7])

        mount_under_test.move_to_position(mount_location, 45)
        for i in range(0, 7):
            self.assertAlmostEqual(mount_under_test.get_sensor(i).current_position()[0],\
                resultant_location[i][0], 6)
            self.assertAlmostEqual(mount_under_test.get_sensor(i).current_position()[1],\
                resultant_location[i][1], 6)
            self.assertAlmostEqual(mount_under_test.get_sensor(i).current_position()[2],\
                resultant_location[i][2], 6)

if __name__ == "__main__":
    unittest.main()
