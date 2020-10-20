#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:40:43 2020

@author: stevenyuan
"""
def counting(n,s):
    '''
    Counting up to n by step with s

    Parameters
    ----------
    n : Int
        The number you want to count up to 
    s : Int
        step

    Returns
    -------
    None. print out the result

    '''
    
    r = ""
    for i in range(1,n+1,s):
        r += str(i) + " "
    print("Counting up to", n, "with step of size", s, ":", r)
    
if __name__ == "__main__":
    counting(25,3)