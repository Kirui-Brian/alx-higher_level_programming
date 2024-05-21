#!/usr/bin/python3
"""
Module: square

Contains the Square class, which represents a square shape.
"""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Parameters:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_pos(position):
            self.__position = position

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        string = ""
        if self.__size == 0:
            string += '\n'
            return string
        for _ in range(0, self.__position[1]):
            string += '\n'
        for _ in range(0, self.__size):
            for _ in range(0, self.__position[0]):
                string += ' '
            for _ in range(0, self.__size):
                string += '#'
            string += '\n'
        return string

    @property
    def size(self):
        """
        Getter method for size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Parameters:
            value (int): The size of the square.
        """
        if self.__validate_size(value):
            self.__size = value

    @property
    def position(self):
        """
        Getter method for position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute.

        Parameters:
            value (tuple): The position of the square.
        """
        if self.__validate_pos(value):
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters and considers the position.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(0, self.__position[1]):
            print()
        for _ in range(0, self.__size):
            for _ in range(0, self.__position[0]):
                print(" ", end='')
            for _ in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        Validates the size input.

        Parameters:
            size (int): The size of the square.

        Returns:
            bool: True if size is valid, False otherwise.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        return True

    def __validate_pos(self, position):
        """
        Validates the position input.

        Parameters:
            position (tuple): The position of the square.

        Returns:
            bool: True if position is valid, False otherwise.
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) and num >= 0 for num in position):
            raise ValueError("position must be a tuple of 2 positive integers")
        return True
