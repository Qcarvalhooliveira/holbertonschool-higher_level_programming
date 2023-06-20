#!/usr/bin/python3
"""Determines if an object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    return issubclass(a_class, type(obj))
