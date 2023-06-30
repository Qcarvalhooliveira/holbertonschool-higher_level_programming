#!/usr/bin/python3
"""Unittest for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json



class TestBaseClass(unittest.TestCase):
   
    @classmethod
    def setUp(self):
        """Set up the environment for unit tests"""
        Base._Base__nb_objects = 0
        pass

    @classmethod
    def tearDownClass(self):
        """Clean up the environment after executing unit tests"""
        pass

    def test_is_private(self):
        """Tests if __nbv_object is private"""
        print('__nbv_object is private')
        self.assertTrue(hasattr(Base, '_Base__nb_objects'), 0)

    def test_docstring(self):
        """Tests the presence of a docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_id_1(self):
        """Tests the ID value for the first instance"""
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_id_2(self):
        """Tests the ID values for multiple instances"""
        base_instance_1 = Base(12)
        base_instance_2 = Base()
        base_instance_3 = Base()
        base_instance_4 = Base()
        self.assertEqual(base_instance_1.id, 12)
        self.assertEqual(base_instance_2.id, 1)
        self.assertEqual(base_instance_3.id, 2)
        self.assertEqual(base_instance_4.id, 3)

    def test_id_3(self):
        """Tests the ID value when passing None as argument"""
        obj = Base(None)
        self.assertEqual(obj.id, 1)

    def test_id_4(self):
        """Tests the ID values for multiple instances"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_string(self):
        """Tests the ID value when passing a string as argument"""
        b1 = Base("Hello")
        self.assertEqual(b1.id, "Hello")

    def test_float(self):
        """Tests the ID value when passing a float as argument"""
        base1 = Base(float('inf'))
        self.assertEqual(base1.id, float('inf'))

    def test_to_json_string(self):
        """Tests the conversion of an object to a JSON string"""
        rect1 = Rectangle(4, 8, 15, 16)
        list_dict = rect1.to_dictionary()
        json_dict = Base.to_json_string([list_dict])
        self.assertEqual(str(type(json_dict)), "<class 'str'>")

    def test_to_json_none(self):
        """Tests the conversion of None to a JSON string"""
        json_empty = Base.to_json_string(None)
        self.assertEqual(json_empty, '[]')

    def test_rectangle_to_file(self):
        """Tests the saving of a Rectangle object to a file"""
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_to_json(self):
        """Tests the conversion of a dictionary to a JSON string"""
        dict1 = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        dict2 = {'id': 89, 'x': 0, 'size': 4, 'y': 3}
        json_string = Base.to_json_string([dict1, dict2])
        jload = json.loads(json_string)
        self.assertEqual(jload, [dict1, dict2])
        self.assertTrue(isinstance(json_string, str))

    def test_from_json_to_str(self):
        """Tests the conversion from JSON string to a list"""
        json_test = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        json_str = Base.from_json_string(json_test)
        self.assertTrue(isinstance(json_str, list))

    def test_from_json_to_str_2(self):
        """Tests the conversion from None to a JSON string, 
        expected to return an empty list"""
        self.assertEqual(Base.from_json_string(None), [])

if __name__ == '__main__':
        unittest.main()
