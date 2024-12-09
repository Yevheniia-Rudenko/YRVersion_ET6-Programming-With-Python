#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 07.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
import unittest

from ..get_length import get_length

class TestGetLength(unittest.TestCase):
    """Test the get_length function"""
    
    def test_list(self):
        """It should return a length value for a non-empty list"""
        self.assertEqual(get_length([1, 2, 3]), 3)
        
    def test_numbers_string(self):
        """It should return the length of a string of numbers"""
        self.assertEqual(get_length('12345'), 5)
    
    def test_string(self):
        """It should return a length value for the string"""
        self.assertEqual(get_length("hello"), 5)

    def test_empty_list(self):
        """It should return None value for an empty list"""
        self.assertIsNone(get_length([]))
    
    def test_empty_string(self):
        """It should return None value for an empty string"""
        self.assertIsNone(get_length(""))

    def test_integer(self):
        """It should raise a TypeError for input like an integer"""
        with self.assertRaises(TypeError):
            get_length(123)
    
    def test_float(self):
        """It should raise a TypeError for input like an float number"""
        with self.assertRaises(TypeError):
            get_length(22.4)
