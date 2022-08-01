#!/usr/bin/python3
"""
Describe a rectangle.
"""
class Rectangle:
"""
Define a rectangle object class
"""
    def __init__(self, width=0, height=0):
    """
    Args:
    width (int): Default width for the class object.
    height (int): Default height for the class object.
    """
        self.__width = width
        self.__height = height

    @property
    def width(self):
    """
    Setter for the private attribute width
    Args:
    None
    Return:
    The return. The private attribute width
    """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sETTER WIDTH OF THE RECTANGLE

        Attributes:
            width (int): The width of the rectagle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height i s not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
