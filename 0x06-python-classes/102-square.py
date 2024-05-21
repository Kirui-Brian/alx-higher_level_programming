#!/usr/bin/python3
"""
Module: square

This module defines a Square class with private instance attribute 'size',
methods to get and set this attribute, methods to calculate the area of
the square, and comparison operators based on the area of the square.
"""


class Square:
    """
    A class that defines a square with a private instance attribute 'size'.

    Attributes:
        __size (int): The size of the square, must be an integer >= 0.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with a size. Validates that size
        is an integer and is >= 0.

        Parameters:
            size (int): The size of the square, default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if self.__validate_size(size):
            self.__size = size

    def __eq__(self, other):
        """
        Checks equality between two Square instances based on their area.

        Parameters:
            other (Square): The other square to compare against.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks inequality between two Square instances based on their area.

        Parameters:
            other (Square): The other square to compare against.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the area of this square is less than another square's area.

        Parameters:
            other (Square): The other square to compare against.

        Returns:
            bool: True if this square's area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of this square is less than or equal to another square's area.

        Parameters:
            other (Square): The other square to compare against.

        Returns:
            bool: True if this square's area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the area of this square is greater than another square's area.

        Parameters:
            other (Square): The other square to compare against.

        Returns:
            bool: True if this square's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of this square is greater than or equal to another square's area.

        Parameters:
            other (Square): The other square to compare against.

        Returns:
            bool: True if this square's area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

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
