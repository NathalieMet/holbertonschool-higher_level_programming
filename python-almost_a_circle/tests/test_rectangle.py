#!/usr/bin/python3
"""Unittest for class base
"""
import unittest
import os
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestBase(unittest.TestCase):

    def setUp(self):
        """Initializing instance with width and height parameters"""
        self.r = Rectangle(5, 10)

    def tearDown(self):
        """Deleting created instance"""
        del self.r

    def test_init_rectangle(self):
        """Tests the __init__ method."""
        r1 = Rectangle(10, 10, 1, 3, 1)
        r2 = Rectangle(20, 20, 2, 4, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r2.y, 4)

        r1 = Rectangle(10, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.y, 0)

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

    def test_area_rectangle(self):
        """Tests the area method."""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

    def test_display_rectangle(self):
        """Tests the display method."""

        r1 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        r2 = Rectangle(3, 2, 1, 0)
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), " ###\n ###\n")

    def test_str_rectangle(self):
        """Tests the str method."""

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (35) 1/0 - 5/5")

    def test_update_rectangle(self):
        """Tests the update method."""

        r1 = Rectangle(1, 1, 2, 2)
        r1.update(45)
        self.assertEqual(str(r1), "[Rectangle] (45) 2/2 - 1/1")
        r1.update(45, 50)
        self.assertEqual(str(r1), "[Rectangle] (45) 2/2 - 50/1")
        r1.update(45, 50, 60)
        self.assertEqual(str(r1), "[Rectangle] (45) 2/2 - 50/60")
        r1.update(45, 50, 60, 70)
        self.assertEqual(str(r1), "[Rectangle] (45) 70/2 - 50/60")
        r1.update(45, 50, 60, 70, 80)
        self.assertEqual(str(r1), "[Rectangle] (45) 70/80 - 50/60")
        with self.assertRaises(IndexError):
            r1.update(45, 50, 60, 70, 80, 90)

        r1.update(height=27)
        self.assertEqual(str(r1), "[Rectangle] (45) 70/80 - 50/27")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (45) 2/80 - 1/27")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/27")

    def test_to_dictionary_rectangle(self):
        """Tests the to_dictionary method."""

        r1 = Rectangle(1, 1, 2, 2, 10)
        self.assertEqual(r1.to_dictionary(), {'id': 10, 'width': 1, 'height': 1, 'x': 2, 'y': 2})

if __name__ == '__main__':
    unittest.main()
