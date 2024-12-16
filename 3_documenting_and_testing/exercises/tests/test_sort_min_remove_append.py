#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
import unittest

from ..sort_min_remove_append import sort_min_remove_append

class TestSortMinRemoveAppend(unittest.TestCase):
    """Test the sort_min_remove_append function"""
    def test_given_a(self):
        """Should return the sorted "a" list"""
        self.assertEqual(sort_min_remove_append([4, 2, 7, 1]), [1, 2, 4, 7])

    def test_given_a_b(self):
        """Should return list when "b" is given"""
        self.assertEqual(sort_min_remove_append([6, 3], [1, 2]), [1, 2, 3, 6])

    def test_duplicates(self):
        """Should return list for input with duplicate"""
        self.assertEqual(sort_min_remove_append([2, 1, 2, 1, 2, 3]), [1, 1, 2, 2, 2, 3])

    def test_empty(self):
        """Should return an empty list when the input list is empty"""
        self.assertEqual(sort_min_remove_append([]), [])

    def test_not_list_input(self):
        """Should raise a TypeError if the input is not a list"""
        with self.assertRaises(TypeError):
            sort_min_remove_append('not a list')

    def test_list_(self):
        """Should raise a TypeError if the second argument is not a list"""
        with self.assertRaises(TypeError):
            sort_min_remove_append([1, 2, 3], 'not a list')
