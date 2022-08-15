#!/usr/bin/python3
"""Creates a class object"""


class Square:
    """Defines a Square"""
    def __init__(self, size=0):
        """Creates a private instance attributte

        properties of the attribute:

        size must be an integer otherwise raise 
        exception TypeError and must be >= 0
        otherise raise exception ValueError.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
