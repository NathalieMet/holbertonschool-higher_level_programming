#!/usr/bin/python3
"""Unittest for class base
"""
import unittest
import os
from models.square import Square

class TestBase(unittest.TestCase):

    def test_init_square(self):
        """Tests the __init__ method."""
        s1 = Square(10, 10, 1, 1)
        s2 = Square(10, 10, 2, 2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

        with self.assertRaises(TypeError):
            s3 = Square("10", "2")

        with self.assertRaises(TypeError):
            s4 = Square(10, "2")

        with self.assertRaises(TypeError):
            s5 = Square(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            s6 = Square()

        with self.assertRaises(TypeError):
            s7 = Square([], {})

    def test_setter_square(self):
        """Tests the width setter method."""

        with self.assertRaises(TypeError):
            s1 = Square(10, 10)
            s1.size = "hello"

        s2 = Square(10, 10)
        s2.size = 20
        self.assertEqual(s2.size, 20)

        with self.assertRaises(ValueError):
            s3 = Square(10, 10)
            s3.size = -10

        with self.assertRaises(TypeError):
            s4 = Square(10, 10)
            s4.size = []

    def test_setter_x_rectangle(self):
        """Tests the x setter method."""

        with self.assertRaises(TypeError):
            r1 = Square(10, 10)
            r1.x = "hello"

        r2 = Square(10, 10)
        r2.x = 20
        self.assertEqual(r2.x, 20)

        with self.assertRaises(ValueError):
            r3 = Square(10, 10)
            r3.x = -10

        with self.assertRaises(TypeError):
            r4 = Square(10, 10)
            r4.x = []

    def test_setter_y_rectangle(self):
        """Tests the y setter method."""

        with self.assertRaises(TypeError):
            r1 = Square(10, 10)
            r1.y = "hello"

        r2 = Square(10, 10)
        r2.y = 20
        self.assertEqual(r2.y, 20)

        with self.assertRaises(ValueError):
            r3 = Square(10, 10)
            r3.y = -10

        with self.assertRaises(TypeError):
            r4 = Square(10, 10)
            r4.y = []

    def test_str_square(self):
        """Tests the str method."""

        s1 = Square(4, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")

        s2 = Square(5, 5, 1)
        self.assertEqual(str(s2), "[Square] (56) 5/1 - 5")

        s3 = Square(5)
        self.assertEqual(str(s3), "[Square] (57) 0/0 - 5")

    def test_update_square(self):
        """Tests the update method."""

        s1 = Square(1, 1, 2, 2)
        s1.update(45)
        self.assertEqual(str(s1), "[Square] (45) 1/2 - 1")
        s1.update(45, 50)
        self.assertEqual(str(s1), "[Square] (45) 1/2 - 50")
        s1.update(45, 50, 60)
        self.assertEqual(str(s1), "[Square] (45) 60/2 - 50")
        s1.update(45, 50, 60, 70)
        self.assertEqual(str(s1), "[Square] (45) 60/70 - 50")
        with self.assertRaises(IndexError):
            s1.update(45, 50, 60, 70, 80)

        s1.update(size=27)
        self.assertEqual(str(s1), "[Square] (45) 60/70 - 27")
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(s1), "[Square] (89) 3/1 - 2")

    def test_to_dictionary_square(self):
        """Tests the to_dictionary method."""

        s1 = Square(1, 2, 2, 10)
        self.assertEqual(s1.to_dictionary(), {'id': 10, 'size': 1, 'x': 2, 'y': 2})

if __name__ == '__main__':
    unittest.main()
