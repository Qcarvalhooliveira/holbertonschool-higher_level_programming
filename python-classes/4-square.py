#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Constructor"""

        self.__size = size
    """size: length of side of the square"""

    @property
    def size(self):
        """Property for the length of a size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
            """TypeError: if size is not an integer"""
            """ValueError: if size < 0 """
        self.__size = value

    def area(self):
        """Square area"""

        return self.__size ** 2
        """Size squared"""
