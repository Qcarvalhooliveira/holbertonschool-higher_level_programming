#!/usr/bin/python3
"""Module for read_file method"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
    f.close()
