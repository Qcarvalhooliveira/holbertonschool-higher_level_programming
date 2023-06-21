#!/usr/bin/python3
"""Import statement that inherits from BaseGeometry (7-base_geometry.py)
and (task based on 8-rectangle.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Determines Rectangle class"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
