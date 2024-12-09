#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function `bubble_sorting` that implements the 
bubble sort algorithm for sorting lists in ascending order.

Module contents:
    - bubble_sorting: Sorts a list of comparable elements in ascending order
    using the bubble sort algorithm.
    
Created on 07.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""

def bubble_sorting(a):
    """
    Sorts a list (a) in ASC order using the bubble sorting algorithm. 

    Parameters:
    List (a): A list of integers, floats, or strings to be sorted. List elements must be of the same type.

    Returns -> The sorted list in ASC order.

    >>> bubble_sorting([3, 7, 6, 1, 5])
    [1, 3, 5, 6, 7]
    
    >>> bubble_sorting([7, 1, 3, 5, 2, 2, 2, 5])
    [1, 2, 2, 2, 3, 5, 5, 7]
    
    >>> bubble_sorting([-1, 3, -5, 6, 2])
    [-5, -1, 2, 3, 6]
    
    >>> bubble_sorting(['a', 'q', 'z', 'c', 's'])
    ['a', 'c', 'q', 's', 'z']  
    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a

#Print the docstring: python3 -m pydoc /Users/yevrud/Desktop/DEVELOPMENT_WORKFLOW/YRVersion_ET6-Programming-With-Python/3_documenting_and_testing/exercises/bubble_sorting.py

#Run the doctests: python3 -m doctest -v /Users/yevrud/Desktop/DEVELOPMENT_WORKFLOW/YRVersion_ET6-Programming-With-Python/3_documenting_and_testing/exercises/bubble_sorting.py
