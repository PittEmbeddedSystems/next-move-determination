#!/usr/bin/env python3

import unittest
from DirectionFinder import DirectionFinder


class DirectionFinderTests(unittest.TestCase):

    def testAllSensorsIdentical(self):
        sensorData = []
        sensorData.append({'amp':128, 'location': (1,1)})
        sensorData.append({'amp':128, 'location': (2,2)})
        sensorData.append({'amp':128, 'location': (3,3)})
        sensorData.append({'amp':128, 'location': (4,4)})
        sensorData.append({'amp':128, 'location': (5,5)})
        sensorData.append({'amp':128, 'location': (6,6)})
        sensorData.append({'amp':128, 'location': (7,7)})
        sensorData.append({'amp':128, 'location': (8,8)})
        testDF = DirectionFinder
        direction = testDF.FindDirection(sensorData)
        
        self.assertEqual(direction, (0,0))

    def testTwoIndependentMaxes(self):
        sensorData = []
        sensorData.append({'amp': 256, 'location': (1, 1)})
        sensorData.append({'amp': 128, 'location': (2, 2)})
        sensorData.append({'amp': 128, 'location': (3, 3)})
        sensorData.append({'amp': 128, 'location': (4, 4)})
        sensorData.append({'amp': 128, 'location': (5, 5)})
        sensorData.append({'amp': 256, 'location': (6, 6)})
        sensorData.append({'amp': 128, 'location': (7, 7)})
        sensorData.append({'amp': 128, 'location': (8, 8)})
        testDF = DirectionFinder
        direction = testDF.FindDirection(sensorData)

        self.assertEqual(direction, (0, 0))


    def testSingleMax(self):
        sensorData = []
        sensorData.append({'amp': 128, 'location': (1, 1)})
        sensorData.append({'amp': 128, 'location': (2, 2)})
        sensorData.append({'amp': 128, 'location': (3, 3)})
        sensorData.append({'amp': 256, 'location': (4, 4)})
        sensorData.append({'amp': 128, 'location': (5, 5)})
        sensorData.append({'amp': 128, 'location': (6, 6)})
        sensorData.append({'amp': 128, 'location': (7, 7)})
        sensorData.append({'amp': 128, 'location': (8, 8)})
        testDF = DirectionFinder
        direction = testDF.FindDirection(sensorData)

        self.assertEqual(direction, (4, 4))

    def testAllZeroAmplitude(self):
        sensorData = []
        sensorData.append({'amp': 0, 'location': (1, 1)})
        sensorData.append({'amp': 0, 'location': (2, 2)})
        sensorData.append({'amp': 0, 'location': (3, 3)})
        sensorData.append({'amp': 0, 'location': (4, 4)})
        sensorData.append({'amp': 0, 'location': (5, 5)})
        sensorData.append({'amp': 0, 'location': (6, 6)})
        sensorData.append({'amp': 0, 'location': (7, 7)})
        sensorData.append({'amp': 0, 'location': (8, 8)})
        testDF = DirectionFinder
        direction = testDF.FindDirection(sensorData)

        self.assertEqual(direction, [])

    def testOneInvalidAmplitude(self):
        sensorData = []
        sensorData.append({'amp': 128, 'location': (1, 1)})
        sensorData.append({'amp': 128, 'location': (2, 2)})
        sensorData.append({'amp': 'Q', 'location': (3, 3)})
        sensorData.append({'amp': 128, 'location': (4, 4)})
        sensorData.append({'amp': 128, 'location': (5, 5)})
        sensorData.append({'amp': 128, 'location': (6, 6)})
        sensorData.append({'amp': 128, 'location': (7, 7)})
        sensorData.append({'amp': 128, 'location': (8, 8)})
        testDF = DirectionFinder
        direction = testDF.FindDirection(sensorData)

        self.assertEqual(direction, (0, 0))


    def testFewerSensors(self):
        sensorData = []
        sensorData.append({'amp': 128, 'location': (1, 1)})
        sensorData.append({'amp': 128, 'location': (2, 2)})
        sensorData.append({'amp': 128, 'location': (3, 3)})
        sensorData.append({'amp': 128, 'location': (4, 4)})
        sensorData.append({'amp': 128, 'location': (5, 5)})
        sensorData.append({'amp': 128, 'location': (6, 6)})
        sensorData.append({'amp': 128, 'location': (7, 7)})
        testDF = DirectionFinder
        direction = testDF.FindDirection(sensorData)

        self.assertEqual(direction, (0, 0))
        assert False

if __name__ == "__main__":
    unittest.main()
