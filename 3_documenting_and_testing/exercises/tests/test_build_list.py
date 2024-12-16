#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
import unittest

from ..build_list import build_list

class TestBuildList(unittest.TestCase):
    """Test the build_list function"""
    def test_positive_number(self):
        """It should return a list, length a-1"""
        self.assertEqual(build_list(4), [0, 1, 2, 3])
    
    def test_negative_number(self):
        """It should return an empty list, a < 0"""
        self.assertEqual(build_list(-2), [])
        
    def test_zero(self):
        """It should return an empty list, a < 0"""
        self.assertEqual(build_list(0), [])
        
    def test_one(self):
        """It should return a list"""
        self.assertEqual(build_list(1), [0])
        
    def test_float(self):
        """It should return a list of integers from 0 to floor(a) - 1"""
        self.assertEqual(build_list(3.5), [0, 1, 2, 3])
        
    def test_string(self):
        """It should raise a TypeError for a string input"""
        with self.assertRaises(TypeError):
            build_list("three")
    
    def test_none_input(self):
        """It should raise a TypeError for a None input"""
        with self.assertRaises(TypeError):
            build_list(None)

    
