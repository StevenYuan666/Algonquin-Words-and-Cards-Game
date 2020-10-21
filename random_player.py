#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:38:07 2020

@author: stevenyuan
"""

import doctest
import random

def draw(hand, top_discard_card):
    '''
    Returns either 'stock' or 'discard' at random 
    (unless there is no top card in the discard pile, 
     in which case only 'stock' should be returned).

    Parameters
    ----------
    hand : list
    top_discard_card : int

    Returns
    -------
    'stock' or 'discard'
    
    >>> random.seed(0)
    >>> draw([4, 50, 15, 21], 5) 
    'discard'
    >>> random.seed(1)
    >>> draw([4, 50, 15, 21], 5) 
    'stock'
    >>> draw([4, 50, 15, 21], None) 
    'stock'
    '''
    choice = ['stock', 'discard']
    if(top_discard_card == None):
        return 'stock'
    else:
        index = random.randint(0, 1)
        return choice[index]
    
def discard(hand):
    '''
    returns a random card in the hand.

    Parameters
    ----------
    hand : list

    Returns
    -------
    Int
    
    >>> random.seed(0)
    >>> discard([4, 50, 15, 21]) 
    21
    >>> random.seed(1)
    >>> discard([4, 50, 15, 21]) 
    50
    >>> random.seed(2)
    >>> discard([4, 50, 15, 21]) 
    4
    >>> random.seed(208)
    >>> discard([4, 50, 15, 21]) 
    15
    '''
    index = random.randint(0, len(hand) - 1)
    return hand[index]

if __name__ == "__main__":
    doctest.testmod()
        