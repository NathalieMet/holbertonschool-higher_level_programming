#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 1]), 1)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([1, 3, 8, 2, -9]), 8)
        self.assertEqual(max_integer([1, 3, 8.5, 2, -9]), 8.5)

if __name__ == '__main__':
    unittest.main()
