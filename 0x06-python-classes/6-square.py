#!/usr/bin/python3
"""
Module: square

This module defines a Square class with private instance attributes 'size'
and 'position', methods to get and set these attributes, a method to
calculate the area of the square, a method to print the square using '#'
characters taking into account position offsets, and private methods to
validate the size and position.
"""


class Square:
    """
    A class that defines a square with private instance attributes 'size'
    and 'position'.

    Attributes:
        __size (int): The size of the square, must be an integer >= 0.
        __position (tuple): The position offset for printing the square,
                            must be a tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square instance with a size and position. Validates
        that size is an integer and is >= 0, and position is a tuple of
        2 positive integers.

        Parameters:
            size (int): The size of the square, default is 0.
            position (tuple): The position offset for printing the square,
                            default is (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                        of 2 positive integers.
            ValueError: If size is less than 0.
        """
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_pos(position):
            self.__position = position

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

    @property
    def position(self):
        """
        Getter for the position attribute.

        Returns:
            tuple: The position offset for printing the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute. Validates that the position is a
        tuple of 2 positive integers.

        Parameters:
            value (tuple): The new position offset for printing the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if self.__validate_pos(value):
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters. Takes into account the
        position (x, y) offsets. If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x_pad in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()

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

    def __validate_pos(self, position):
        """
        Validates the position, checking for type errors.

        Parameters:
            position (tuple): The position to validate.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.

        Returns:
            bool: True if position is valid, False otherwise.
        """
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(num, int)
                and
                num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        return True
