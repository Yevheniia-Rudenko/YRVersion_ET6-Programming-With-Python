#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function build_list that generates a list of numbers from 0 to the specified length(a) minus one.

Module contents:
	- build_list(a): A function that creates and returns a list of integers starting from 0 up to a-1, where a is the input parameter representing the desired length of the list.
    
Created on 10.12.2024

@author: Evan Cole, Yevheniia Rudenko
"""
def build_list(a):
    """ Generates a list of numbers, length is a-1.
    Parameters:
	- a (int): The length of the list to be generated.

    Returns -> A list of integers from 0 to a-1.
    
    >>> build_list(3)
    [0, 1, 2]
    
    >>> build_list(1)
    [0]
    
    >>> build_list(-5)
    []
    
    """
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
