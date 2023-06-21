#!/usr/bin/python3
"""Import statement that inherits from Rectangle (9-rectangle.py)
and (task based on 10-square.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Determines Square class"""

    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
