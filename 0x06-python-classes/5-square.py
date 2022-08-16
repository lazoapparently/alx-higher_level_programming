#!/usr/bin/python3
"""
Creates a class Square width:
    -size property
    - method of area and method of print_square
    - getters and setters.
"""


class Square:
    """Define a class square"""
    def __init__(self, size=0):
        """Creates a square with the size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """Method of area of a square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method to print square"""
        if (self.__size == 0):
            print()
        else:
            for rows in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """Getter for the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for private attribute size"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
