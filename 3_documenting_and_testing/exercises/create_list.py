#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function create_list that generates a list of numbers starting from the specified value b and adds b + 1 with each iteration until the list reaches the specified length a.

Module contents:
	- create_list(a, b): A function that creates and returns a list of integers starting from b and incrementing by 1, with the list length equal to a.

Created on 12.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
def create_list(a, b):
    """ Generates a list of numbers starting from b, with a length of a.
    Parameters:
    - a (int): The length of the list to be generated.
    - b (int): The starting number of the list.

    Returns -> A list of integers starting from b and incrementing by 1 until the list length reaches a.

    >>> create_list(3, 5)
    [5, 6, 7]

    >>> create_list(1, 2)
    [2]

    >>> create_list(0, 10)
    []
    """
    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
