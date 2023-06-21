#!/usr/bin/python3
"""Module to Write a class BaseGeometry"""


class BaseGeometry:
    def __init__(self):
        """Constructor"""
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """instance method that validates value"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
