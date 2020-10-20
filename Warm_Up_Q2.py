#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:31:51 2020

@author: stevenyuan
"""
import Warm_Up_Q1 as w

#create two global variable
x = 3
y = 4

if __name__ == "__main__":
    w.swap(3,4)
    print(x)
    print(y)
    
    #the value will not be changed, since we just swap the local variable
    #inside the function swap, so it has no effect on the global variables

