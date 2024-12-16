#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function `sort_min_remove_append` that sorts a list by removing its smallest elements by iteration and appending them to another list.

Module contents:
    - sort_min_remove_append: A function that sorts a given list in ascending order by removing its minimum elements and appending them to another list. The sorted result is returned.
"""

def sort_min_remove_append(a, b=None):
    """
    Sorts a list by iter. removing the smallest element and appending it to another list.

    Parameters:
        a (list): The input list to be sorted. This list will be modified in place and become empty.
        b (list, optional): An optional list to which the sorted elements will be appended.

    Returns -> list: A list containing the sorted elements of the input list "a",inserted or appended to "b" list.
        
    >>> sort_min_remove_append([4, 2, 7, 1])
    [1, 2, 4, 7]
        
    >>> sort_min_remove_append([6, 3], [1, 2])
    [1, 2, 3, 6]
        
    >>> sort_min_remove_append([2, 1, 2, 1, 2, 3])
    [1, 1, 2, 2, 2, 3]
        
    >>> sort_min_remove_append([])
    []
    """
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
