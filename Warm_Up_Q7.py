#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:54:37 2020

@author: stevenyuan
"""
import random
import doctest

def generate(n):
    '''
    Generate a list with n random integers between 0 to 100

    Parameters
    ----------
    n : Int

    Returns
    -------
    List with length n

    >>> random.seed(0)
    >>> generate(10)
    [49, 97, 53, 5, 33, 65, 62, 51, 100, 38]
    >>> random.seed(1205)
    >>> generate(10)
    [83, 52, 97, 97, 89, 51, 92, 80, 58, 46]
    '''
    r = []
    for i in range(n):
        tmp = random.randint(0, 100)
        r.append(tmp)
    return r

if __name__ == "__main__":
    doctest.testmod()