#!/usr/bin/env python3


class DirectionFinder:
    """
    The class is responsible for finding the Angle Of Arrival (AOA) of
    light based on the current sensor data.
    """


    def FindDirection(sensorData):
        """
        This method takes an array of sensor data and estimates the AOA of the
        light. it requires each sensor element to include the current amplitude
        measurement as well as its own position relative to some origin. The AOA
        will be relative to the same origin.

        This implementation is simple in that it does not attempt to interpolate
        between sensor positions. More sophisticated implementations should override
        this method.
        """
        maxAmp = 0
        maxDirection = { 0, 0 }
        
        for element in sensorData:
            if element[amp] > maxAmp:
                maxDirection = element[location]

        return maxDirection
