#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function `get_length` that calculate the length of the input.

Module contents:
    - get_length: A function that returns the length of the given input or `None` if it is empty.
    
Created on 07.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
def get_length(a):
    """Calculates the length of the input(a).

    Parameters:
    - a: An input object (list, string) whose length needs to be calculated.

    Returns -> The length of the input object if it is not empty, or `None` if the input is empty.
    
    >>> get_length([2, 1, 2, 1, 2, 3])
    6
    
    >>> get_length("Hello")
    5
    
    >>> get_length(('a', 'b'))
    2
    
    >>> get_length([])
    
    """
    if len(a) == 0:
        return None

    return len(a)
