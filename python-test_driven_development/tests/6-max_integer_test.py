#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with max value at the beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_single_element_list(self):
        """Test a list with a single element."""
        single_element = [7]
        self.assertEqual(max_integer(single_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Hello"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Hello", "World", "Python"]
        self.assertEqual(max_integer(strings), "World")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertIsNone(max_integer(""))

if __name__ == '__main__':
    unittest.main()