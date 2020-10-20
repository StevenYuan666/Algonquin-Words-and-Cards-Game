#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:27:20 2020

@author: stevenyuan
"""
import doctest

def swap(x, y):
    '''
    Swap the value of x and y

    Parameters
    ----------
    x : Int
    y : Int
    Returns
    -------
    None. Print the value of each after swapping

    >>> swap(3,4)
    The value of x before swapping 3
    The value of y before swapping 4
    The value of x after swapping 4
    The value of y after swapping 3
    '''
    print('The value of x before swapping', x)
    print('The value of y before swapping', y)
    tmp = x
    x = y
    y = tmp
    print('The value of x after swapping', x)
    print('The value of y after swapping', y)
    
if __name__ == "__main__":
    doctest.testmod()