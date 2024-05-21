#!/usr/bin/python3
"""
Module: square

This module defines a Square class with a private instance attribute 'size'
and a method to calculate the area of the square.
"""


class Square:
    """
    A class that defines a square with a private instance attribute 'size'.

    Attributes:
        __size (int): The size of the square, must be an integer >= 0.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with a size. Validates that size is
        an integer and is >= 0.

        Parameters:
            size (int): The size of the square, default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
