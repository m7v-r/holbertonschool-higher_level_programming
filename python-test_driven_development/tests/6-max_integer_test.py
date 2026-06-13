#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list where the max values is at the beginning."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_no_args(self):
        """Test max_integer with no arguments passed."""
        self.assertEqual(max_integer(), None)

    def test_one_element_list(self):
        """Test a list with only one element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_all_negative_numbers(self):
        """Test a list consisting only of negative integers."""
        all_negative = [-1, -2, -3, -4]
        self.assertEqual(max_integer(all_negative), -1)

    def test_mixed_numbers(self):
        """Test a list with both positive and negative integers."""
        mixed = [-10, 15, -2, 0, 4]
        self.assertEqual(max_integer(mixed), 15)


if __name__ == '__main__':
    unittest.main()
