#!/usr/bin/python3
"""Module to returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a class"""
    return issubclass(a_class, type(obj))
