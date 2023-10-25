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

    def test_setter_width_rectangle(self):
        """Tests the width setter method."""

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10)
            r1.width = "hello"

        r2 = Rectangle(10, 10)
        r2.width = 20
        self.assertEqual(r2.width, 20)

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 10)
            r3.width = -10

        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 10)
            r4.width = []

        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 10)
            r5.width = 0

    def test_setter_height_rectangle(self):
        """Tests the width setter method."""

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10)
            r1.height = "hello"

        r2 = Rectangle(10, 10)
        r2.height = 20
        self.assertEqual(r2.height, 20)

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 10)
            r3.height = -10

        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 10)
            r4.height = []

        with self.assertRaises(ValueError):
            r5 = Rectangle(10, 10)
            r5.height = 0

    def test_setter_x_rectangle(self):
        """Tests the x setter method."""

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10)
            r1.x = "hello"

        r2 = Rectangle(10, 10)
        r2.x = 20
        self.assertEqual(r2.x, 20)

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 10)
            r3.x = -10

        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 10)
            r4.x = []

    def test_setter_y_rectangle(self):
        """Tests the y setter method."""

        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10)
            r1.y = "hello"

        r2 = Rectangle(10, 10)
        r2.y = 20
        self.assertEqual(r2.y, 20)

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 10)
            r3.y = -10

        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 10)
            r4.y = []

if __name__ == '__main__':
    unittest.main()
