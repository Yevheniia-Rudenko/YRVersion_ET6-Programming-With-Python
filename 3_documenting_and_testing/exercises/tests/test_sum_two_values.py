#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 07.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
import unittest

from ..sum_two_values import sum_two_values

class TestSumTwoValues(unittest.TestCase):
    """Test the sum_two_values function"""
    def test_sum_integers(self):
        """It should sum two integers"""
        self.assertEqual(sum_two_values(3, 5), 8)
        
    def test_sum_floats(self):
        """It should sum two float numbers"""
        self.assertEqual(sum_two_values(3.5, 5.2), 8.7)
        
    def test_sum_integer_and_float(self):
        """It should sum integer with float number"""
        self.assertEqual(sum_two_values(3, 5.5), 8.5)
        
    def test_sum_negative_integers(self):
        """It should sum two negative integers"""
        self.assertEqual(sum_two_values(-3, -5), -8)
    
    def test_sum_mixed_negative_and_positive(self):
        """It should sum negative integer with positive integer"""
        self.assertEqual(sum_two_values(-3, 5), 2)
    
    def test_invalid_input_string(self):
        """It should raise a TypeError for invalid (str) input"""
        with self.assertRaises(TypeError):
            sum_two_values("a", 5)
            
    def test_empty_string_input_first(self):
        """It should raise a TypeError for invalid (empty str) input"""
        with self.assertRaises(TypeError):
            sum_two_values("", 5)
            
    def test_empty_input_both(self):
        """It should raise a TypeError for invalid (None) input"""
        with self.assertRaises(TypeError):
            sum_two_values(None, None)
