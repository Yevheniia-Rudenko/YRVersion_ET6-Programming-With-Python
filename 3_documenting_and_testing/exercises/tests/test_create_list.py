#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 12.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
import unittest

from ..create_list import create_list

class TestCreateList(unittest.TestCase):
    """Test the create_list function"""

    def test_positive_length(self):
        """It should return a list starting from b with length a"""
        self.assertEqual(create_list(3, 5), [5, 6, 7])

    def test_single_element(self):
        """It should return a list with one element if a is 1"""
        self.assertEqual(create_list(1, 2), [2])

    def test_zero_length(self):
        """It should return an empty list if a is 0"""
        self.assertEqual(create_list(0, 10), [])

    def test_large_numbers(self):
        """It should handle large numbers"""
        self.assertEqual(create_list(5, 1000), [1000, 1001, 1002, 1003, 1004])

    def test_negative_start(self):
        """It should handle negative b value"""
        self.assertEqual(create_list(3, -2), [-2, -1, 0])

    def test_negative_length(self):
        """It should return an empty list if a is negative"""
        self.assertEqual(create_list(-3, 5), [])

    def test_type_error_non_integer_length(self):
        """It should raise a TypeError if a is not an integer"""
        with self.assertRaises(TypeError):
            create_list("3", 5)

    def test_type_error_non_integer_start(self):
        """It should raise a TypeError if b  is not an integer"""
        with self.assertRaises(TypeError):
            create_list(3, "5")
