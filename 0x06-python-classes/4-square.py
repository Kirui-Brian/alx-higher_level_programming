#!/usr/bin/python3
"""
Module: square

This module defines a Square class with a private instance attribute 'size',
methods to get and set the size, a method to calculate the area of the square,
and a private method to validate the size.
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
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute. Validates that the size is an integer
        and is >= 0.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __validate_size(self, size):
        """
        Validates the size, checking for errors.

        Parameters:
            size (int): The size to validate.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            bool: True if size is valid, False otherwise.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        return True
