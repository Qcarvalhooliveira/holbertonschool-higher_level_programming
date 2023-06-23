#!/usr/bin/python3
"""Module for load_to_json_file method"""


import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename, 'r',) as json_file:
        my_obj = json.load(json_file)
        return my_obj
