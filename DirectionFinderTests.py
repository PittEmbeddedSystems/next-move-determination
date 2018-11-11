#!/usr/bin/env python3

import unittest
import DirectionFinder


class DirectionFinderTests(unittest.TestCase):

    def testAllSensorsIdentical(self):
        assert 0 == 1

    def testTwoIndependentMaxes(self):
        assert False

    def testSingleMax(self):
        assert False

    def testAllZeroAmplitude(self):
        assert False

    def testOneInvalidAmplitude(self):
        assert False

if __name__ == "__main__":
    unittest.main()
