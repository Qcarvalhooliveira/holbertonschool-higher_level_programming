#!/usr/bin/python3
""" class MyList that inherits from list"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        print(sorted(self))
