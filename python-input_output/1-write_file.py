#!/usr/bin/python3
"""Module for write_file method"""


def write_file(filename="", text=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
