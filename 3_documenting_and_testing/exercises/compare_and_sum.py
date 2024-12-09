#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function `compare_and_sum` that compares two input values. 
If one value is smaller, it returns the smaller value. 
If the values are equal, it returns their sum.

Module contents:
    - compare_and_sum: Compares two input values and returns the smaller value if they are different, or their sum if they are equal. 

Created on 07.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
def compare_and_sum(a, b):
    """
    Compares two input values, and sums them up if they are equal. Otherwise, it returns the smaller value.

    Parameters:
    - a: The first input value (can be int, float, string).
    - b: The second input value (can be int, float, string).

    Returns ->  The smaller value if the values are different, or the sum of the values if they are equal.
    
    >>> compare_and_sum(3, 5)
    3
    
    >>> compare_and_sum(8, 8)
    16
    
    >>> compare_and_sum('a', 'b')
    'a'
    
    >>> compare_and_sum(32.4, 88.3)
    32.4
    
"""

    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
