#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function `sum_two_values` that sums two numbers.

Module contents:
- A function `sum_two_values` that takes two numerical values and returns their sum.
    
Created on 07.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
def sum_two_values(a,b):
    """ 
    Sum two numerical values.

    Parameters:
    a (number): First int or float number.
    b (number): Second int or float number.

    Returns -> Sum of a and b.
    
    >>> sum_two_values(2, 5)
    7
    
    >>> sum_two_values(2.5, 2.1)
    4.6
    
    >>> sum_two_values(-3, 2)
    -1
    """
    return a + b
