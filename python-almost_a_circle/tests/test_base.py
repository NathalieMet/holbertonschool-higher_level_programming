#!/usr/bin/python3
"""Unittest for class base
"""
import unittest
import json
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_init(self):
        """Tests the __init__ method."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

        b3 = Base(-10)
        self.assertEqual(b3.id, -10)

        b4 = Base(100)
        self.assertEqual(b4.id, 100)

        b5 = Base("hello")
        self.assertEqual(b5.id, "hello")


        with self.assertRaises(TypeError):
            b6 = Base(1, 2, 3)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        list_dictionaries = [{"key1": "value1"}, {"key2": "value2"}]
        self.assertEqual(Base.to_json_string(list_dictionaries), json.dumps(list_dictionaries))

    def test_save_to_file(self):
        obj = Base()
        obj.id = 1

        Base.save_to_file([obj])

        self.assertTrue(os.path.exists('Base.json'))

        with open('Base.json', 'r') as f:
            content = f.read()
            self.assertEqual(content, Base.to_json_string([obj.to_dictionary() if isinstance(obj, Rectangle) else obj.__dict__]))

        os.remove('Base.json')

if __name__ == '__main__':
    unittest.main()
