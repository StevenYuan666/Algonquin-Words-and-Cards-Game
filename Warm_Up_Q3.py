#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:35:20 2020

@author: stevenyuan
"""

def count(n):
    '''
    Count from 1 to n

    Parameters
    ----------
    n : Int
        The number you want to count up to
        
    Returns
    -------
    None. Print out the counting result

    '''
    l = ""
    for i in range(10):
        l += str((i + 1)) + " "
        
    print("Counting up to ", n, ":",l)
    
if __name__ == "__main__":
    count(10)