#!/usr/bin/python3
"""Module that determines if the object is an instance of,
    or if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """Determines if the object is an instance of,
    or if the object is an instance"""
    return isinstance(obj, a_class) or isinstance(a_class, type(obj))
