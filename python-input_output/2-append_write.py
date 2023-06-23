#!/usr/bin/python3
"""Module for append_file method"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)"""
    with open(filename, 'a', encoding='utf-8') as append_file:
        return (append_file.write(text))
