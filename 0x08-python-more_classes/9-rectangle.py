#!/usr/bin/python3
"""
Module: 9-rectangle

This module defines a Rectangle class with private instance attributes
for width and height, and includes property getters and setters
to ensure these attributes are valid integers. It also includes public
class attributes to count the number of instances created and to set
the symbol for string representation of the rectangle. It also includes
methods to calculate the area and perimeter of the rectangle and to print
it using the specified symbol. It also includes a method to return a string
representation that can be used with eval(), a static method to compare two
rectangles by area, a class method to create a square, and a message when
an instance is deleted.
"""


class Rectangle:
    """
    A class that defines a rectangle with private instance attributes
    for width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance with optional width and height.

        Parameters:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        Validates that the width is an integer and is >= 0.

        Parameters:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        Validates that the height is an integer and is >= 0.

        Parameters:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle. If width or height is 0,
                 the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle, using the character
        specified by print_symbol to represent the rectangle.
        If width or height is 0, returns an empty string.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = "\n".join(
                [str(self.print_symbol) * self.__width
                    for _ in range(self.__height)]
                )
        return rectangle_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used
        to recreate a new instance using eval().

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the greater area.
        If the areas are equal, returns the first rectangle.

        Parameters:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the greater area, or the first
                       rectangle if the areas are equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance where width and height are equal.

        Parameters:
            size (int):
            The size of the new rectangle's width and height. Default is 0.

        Returns:
            Rectangle:
            A new Rectangle instance with width and height set to size.
        """
        return cls(size, size)
