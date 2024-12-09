#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 07.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""

import unittest
from ..bubble_sorting import bubble_sorting


class TestBubbleSort(unittest.TestCase):
    """Test the bubble_sorting function"""

    def test_empty_list(self):
        """It should return an empty list for an empty input"""
        self.assertEqual(bubble_sorting([]), [])

    def test_single_element(self):
        """It should return the same list when it contains only one element"""
        self.assertEqual(bubble_sorting([5]), [5])

    def test_already_sorted(self):
        """It should return the same list if the list is already sorted"""
        self.assertEqual(bubble_sorting([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        """It should sort the list in ascending order"""
        self.assertEqual(bubble_sorting([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        """It should handle lists with duplicate values"""
        self.assertEqual(bubble_sorting([1, 3, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        """It should handle lists with negative numbers"""
        self.assertEqual(bubble_sorting([3, -2, 5, -1, 4]), [-2, -1, 3, 4, 5])

    def test_large_numbers(self):
        """It should handle large numbers correctly"""
        self.assertEqual(bubble_sorting([999999, 1, 555555, 333333, 777777]), [1, 333333, 555555, 777777, 999999])

    def test_floats(self):
        """It should sort a list containing float values"""
        self.assertEqual(bubble_sorting([1.1, 2.2, 3.3, 0.5]), [0.5, 1.1, 2.2, 3.3])

    def test_strings(self):
        """It should sort a list containing string values"""
        self.assertEqual(bubble_sorting(["apple", "orange", "banana", "grape"]), ["apple", "banana", "grape", "orange"])

    def test_invalid_input(self):
        """It should raise a TypeError for invalid input"""
        with self.assertRaises(TypeError):
            bubble_sorting([1, "two", 3.0])


# Run the unit tests: python3 -m unittest /Users/yevrud/Desktop/DEVELOPMENT_WORKFLOW/YRVersion_ET6-Programming-With-Python/3_documenting_and_testing/exercises/tests/test_bubble_sorting.py
