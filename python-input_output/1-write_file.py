#!/usr/bin/python3
"""Module for write_file method"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)"""
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
