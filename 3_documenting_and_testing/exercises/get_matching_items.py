#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function get_matching_items that filters a list and returns only the elements that contain a specified value - b.

Module contents:
    - get_matching_items(a, b): A function that filters a list a, returning elements that contain b.

Created on 12.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
def get_matching_items(a, b):
    """ Filters a list, returning elements that contain "b" within.
    
    Parameters:
    - a (list): The list to be filtered.
    - b: The value to be searched within the elements of the list.

    Returns -> A list,  only with elements that include b.

    >>> get_matching_items(["apple", "banana", "cherry", "grape"], "a")
    ['apple', 'banana', 'grape']

    >>> get_matching_items([[1, 2], [3, 4], [5, 6, 2]], 2)
    [[1, 2], [5, 6, 2]]

    >>> get_matching_items(["hello", "world", "python"], "z")
    []
    """
    c = []
    for d in a:
        if b in d:
            c.append(d)
    return c
