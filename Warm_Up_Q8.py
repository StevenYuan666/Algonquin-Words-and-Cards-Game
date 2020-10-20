#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:00:32 2020

@author: stevenyuan
"""

import doctest

def sum_up(l):
    '''
    Input a list, return the sum of every element in the list

    Parameters
    ----------
    l : list

    Returns
    -------
    Sum of the every element in the list

    >>> sum_up([1,2,3])
    6
    '''
    
    s = 0
    for e in l:
        s += e
    return s

if __name__ == "__main__":
    doctest.testmod()