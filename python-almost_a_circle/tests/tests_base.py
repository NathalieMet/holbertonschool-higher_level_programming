#!/usr/bin/python3
"""Unittest for class base
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        """Tests the __init__ method."""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

        b4 = Base(100)

        self.assertEqual(b4.id, 100)

if __name__ == '__main__':
    unittest.main()
