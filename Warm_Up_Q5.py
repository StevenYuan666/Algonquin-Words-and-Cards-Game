#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:44:49 2020

@author: stevenyuan
"""
import doctest

def replace_all(s, c1, c2):
    '''
    Replace the character c1 in s with character c2

    Parameters
    ----------
    s : String
        The string will be modified
    c1 : char
        the character will be replaced
    c2 : char
        the character to replace c1

    Returns
    -------
    The modified string

    >>> replace_all("squirrel", "r" , "s")
    'squissel'
    >>> replace_all("squirrel", "t", "a")
    'squirrel'
    '''
    r = ""
    for c in s:
        if(c == c1):
            r += c2
        else:
            r += c
    return r

if __name__ == "__main__":
    doctest.testmod()