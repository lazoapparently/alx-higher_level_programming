#!/usr/bin/python3
# -*- coding: utf-8 -*-

class rectangle:
    """
    class rectangle defines a rectangle figure

    Attributes:
        empty
    """

    def __init__(self, width=0, height=0):
        """
        Init method for rectangle

        Attributes:
            width (int, optional): The width of the rectangle
            height (int, optional): The height of the rectangle
        self.width = width
        self.height = height
        """
        self.__height = height
        self.__width = width

    def __str__(self):
        """
        str method to print rectangle

        Returns:
            string : The string with no of rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i < self.__height - 1:
                string += '\n'
        return string

    @property
    def height(self):
        """
        Property height to retrive

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height
    @property
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height (int): the height of the rectangle


        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width (int): the width of the rectangle
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

    def area(self):
        """
        Calculate the area of the rectangle

        Returns
            The area of the rectagle
        """
        return self.__width * self.__height
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
