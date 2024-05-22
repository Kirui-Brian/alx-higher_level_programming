#!/usr/bin/python3
"""
This module provides a function 'add_integer' that adds two integers.

Example:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(4.5, 3.1)
    7
    >>> add_integer(-2, -3.9)
    -5
    >>> add_integer(2.5)
    100
    >>> add_integer(float('inf'), 1)
    Traceback (most recent call last):
        ...
    OverflowError: cannot convert float infinity to integer
    >>> add_integer(3, float('nan'))
    Traceback (most recent call last):
        ...
    ValueError: cannot convert float NaN to integer
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, defaults to 98.

    Returns:
        int: The sum of a and b after casting them to integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
