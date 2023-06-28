#!/usr/bin/python3
"""Module for class Base"""

from json import dumps


class Base:
    """Class Base that defines a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)
