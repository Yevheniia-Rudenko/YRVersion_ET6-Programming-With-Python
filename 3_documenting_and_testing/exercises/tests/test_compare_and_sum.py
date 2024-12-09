#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 07.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
import unittest

from ..compare_and_sum import compare_and_sum

class TestCompareAndSum(unittest.TestCase):
    """Test the compare_and_sum function  """
    def test_smaller_int_value(self):
        # It should return the smaller int value 
        self.assertEqual(compare_and_sum(3, 5), 3)
        
    def test_smaller_str_value(self):
        # It should return the smaller str value 
        self.assertEqual(compare_and_sum('a', 'b'), 'a')
    
    def test_equal_int_values(self):
        # It should return the sum of the int values when they are equal
        self.assertEqual(compare_and_sum(8, 8), 16)
        
    def test_equal_str_values(self):
        # It should return the sum of the str values when they are equal
        self.assertEqual(compare_and_sum('test', 'test'), 'testtest')
        
    def test_equal_values(self):
        # It should return the sum of the float values when they are equal
        self.assertEqual(compare_and_sum(0.5, 0.5), 1.0)
    
    def test_mixed_types(self):
        # It should return the sum when the values are considered equal
        self.assertEqual(compare_and_sum(5, 5.0), 10.0)
    
    def test_string_comparison(self):
        # It should return the smaller string if they are not equal
        self.assertEqual(compare_and_sum('apple', 'banana'), 'apple')
    
    def test_none_values(self):
        # It should raise a TypeError when None is passed since the function is not expected to handle None
        with self.assertRaises(TypeError):
            compare_and_sum(None, 'abc')
