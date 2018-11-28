#!/usr/bin/env python3


class DirectionFinder:
    """
    The class is responsible for finding the Angle Of Arrival (AOA) of
    light based on the current sensor data.
    """


    def FindDirection(self, sensorData):
        """
        This method takes an array of sensor data and estimates the AOA of the
        light. it requires each sensor element to include the current amplitude
        measurement as well as its own position relative to some origin. The AOA
        will be relative to the same origin.

        NOTE: If the data provided is determined to be invalid, this method returns
        an empty vector - () which indicates that the AOA could not be determined.

        This implementation is simple in that it does not attempt to interpolate
        between sensor positions. More sophisticated implementations should override
        this method.
        """
        maxAmp = 0
        maxDirection = { 0, 0 }

        # Special Case: If all elements are the same, don't move anywhere
        if all(element['amp'] == sensorData[0]['amp'] for element in sensorData):
            return (0, 0)

        for element in sensorData:
            # If any of the amplitudes aren't valid, then return an invalid result
            if not str(element['amp']).isdecimal():
                print("Error: Invalid amplitude (" + str(element['amp']) + ") from sensor at position " + str(element['location']))
                return ()

            if element['amp'] > maxAmp:
                maxAmp = element['amp']
                maxDirection = element['location']

        return maxDirection
