#!/usr/bin/python3
"""
Defines a class rectangle.
"""

class Rectangle:
    """Define a rectangle object class"""
    def __init__(self, width=0, height=0):
    """Initializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
    """The private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
