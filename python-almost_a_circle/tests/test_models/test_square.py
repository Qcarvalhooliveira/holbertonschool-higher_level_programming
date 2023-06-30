#!/usr/bin/python3
"""Unittest for square.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestSquareClass(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """Set up the test environment by resetting the counter
           and creating Square instances"""
        Base._Base__nb_objects = 0
        cls.sqr1 = Square(2, 4)
        cls.sqr2 = Square(2, 4, 6)
        cls.sqr3 = Square(2, 4, 6, 8)
        cls.sqr4 = Square(2, 4, 8, 10)

    @classmethod
    def tearDownClass(self):
        """Clean up the test environment after running all the tests"""
        pass

    def test_class(self):
        """Test if the class name is correct"""
        self.assertTrue(str(Square), "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        """Test if Square inherits from Base class"""
        self.assertTrue(issubclass(Square, Base))

    def test_values(self):
        """Test if the size value is assigned correctly"""
        sqr1 = Square(3)
        self.assertEqual(sqr1.size, 3)

    def test_str(self):
        """Test the string representation of Square objects"""
        sqr1 = Square(3)
        sqr2 = Square(4, 5, 6)
        self.assertEqual(sqr1.__str__(), '[Square] (3) 0/0 - 3')
        self.assertEqual(sqr2.__str__(), '[Square] (4) 5/6 - 4')

    def test_area(self):
        """Test the area calculation for a Square"""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_save_to_file(self):
        """Test saving Square objects to a file"""
        Square.save_to_file(None)
        with open('Square.json', 'r') as f:
            self.assertEqual('[]', f.read())

    def test_save_load_file(self):
        """Test saving and loading Square objects from a file"""
        r1 = Square(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Square.save_to_file([r1, r2])
        load_file = Square.load_from_file()
        self.assertTrue(isinstance(load_file, list))

    def test_to_dict(self):
        """Test converting Square object to a dictionary"""
        dict1 = self.sqr1.to_dictionary()
        self.assertEqual({'id': 1, 'size': 2, 'x': 4, 'y': 0}, dict1)
        self.assertTrue(isinstance(dict1, dict))

if __name__ == '__main__':
            unittest.main()
