#!/usr/bin/python3
import math

"""
This module defines the MagicClass which represents a circle with a given
radius. It can calculate the area and circumference of the circle.
"""


class MagicClass:
    """
    This class represents a circle with a given radius.
    It can calculate the area and circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass with a given radius.

        Parameters:
            radius (int or float): The radius of the circle. Default is 0.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
