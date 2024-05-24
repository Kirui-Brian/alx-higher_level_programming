#!/usr/bin/python3
"""
This module defines the LockedClass.

Attributes:
    LockedClass: A class that prevents dynamic attribute creation, except if the new instance attribute is called 'first_name'.
"""

class LockedClass:
    """
    A class that locks attribute creation to prevent dynamic creation of attributes.

    This class uses the `__slots__` magic attribute to lock the allowable attributes that instances of this class can have.

    Attributes:
        first_name (str): The first name of the instance.
    """
    __slots__ = ['first_name']
