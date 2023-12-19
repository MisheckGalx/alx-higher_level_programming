#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """ This class represents a square with a given size.
    """

    def __init__(self, size=0):
        """ This method initializes the square object with a size.
        """
        if not isinstance(size, int):
            raise TypeError("The size must be an integer.")
        elif size < 0:
            raise ValueError("The size must be a non-negative integer.")
        else:
            self.__size = size

    def area(self):
        """ This method calculates and returns the area of the square.
        """
        return (self.__size ** 2)
