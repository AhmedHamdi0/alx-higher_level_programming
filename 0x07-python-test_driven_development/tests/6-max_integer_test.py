#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -3, 4, -2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_elements(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)
        self.assertEqual(max_integer([-5, -5, -5]), -5)

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 3, 'b'])

    def test_non_list_input(self):
        with self.assertRaises(KeyError):
            max_integer({1: 'a'})


if __name__ == '__main__':
    unittest.main()
