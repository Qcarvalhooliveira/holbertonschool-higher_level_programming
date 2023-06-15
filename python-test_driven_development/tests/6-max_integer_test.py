#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_max_integer(self):
        my_list = [1, 3, 4, 2]
        self.assertEqual(max_integer(my_list), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
