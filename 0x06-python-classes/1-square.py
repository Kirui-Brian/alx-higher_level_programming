#!/usr/bin/python3
"""
Module: square

This module defines a Square class with an attribute size.
"""


class Square:
    """
    A class that defines a square with a private instance attribute 'size'.

    Attributes:
        __size (int): The size of the square.
    """


    def __init__(self, size):
        """
        Initializes the Square instance with a size.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size
