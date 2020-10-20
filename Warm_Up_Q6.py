#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:49:31 2020

@author: stevenyuan
"""

import doctest
lower_alpha = "abcdefghijklmnopqrstuvwxyz" 
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def make_lower(s):
    '''
    Make the inpur string s to lower case

    Parameters
    ----------
    s : String

    Returns
    -------
    Lower case string s

    >>> make_lower("AppLE")
    'apple'
    '''
    
    
    r = ""
    for c in s:
        if(c in upper_alpha):
            index = upper_alpha.find(c)
            r += lower_alpha[index]
        else:
            r += c
    return r

if __name__ == "__main__":
    doctest.testmod()