#!/usr/bin/python3
"""Unittest for class base
"""
import unittest
import os
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):

    def setUp(self):
        """Initializing instance with width and height
        parameters"""
        self.r = Rectangle(5, 10)

    def tearDown(self):
        """Deleting created instance"""
        del self.r

    def test_init_rectangle(self):
        """Tests the __init__ method."""
        r1 = Rectangle(10, 10, 1, 1, 1)
        r2 = Rectangle(10, 10, 2, 2, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

        with self.assertRaises(TypeError):
            r3 = Rectangle("10", "2")

        with self.assertRaises(TypeError):
            r4 = Rectangle(10, "2")

        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r6 = Rectangle()

        with self.assertRaises(TypeError):
            r7 = Rectangle([], {})

if __name__ == '__main__':
    unittest.main()
