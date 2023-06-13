#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """ size: length of side of the square
            TypeError: if size is not an integer
            ValueError: if size < 0 """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
