#!/usr/bin/python3
"""Module for class_to_json method"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
