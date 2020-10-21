#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:12:46 2020

@author: stevenyuan
"""

import doctest
import card1
import card2

def calculate_winner(points):
    '''
    eturns a list containing the indices of the list 
    corresponding to the lowest points in the points list.

    Parameters
    ----------
    points : list

    Returns
    -------
    list

    >>> calculate_winner([100, 5, 20, 42]) 
    [1]
    >>> calculate_winner([100, 5, 20, 5]) 
    [1, 3]
    '''
    indices = []
    minimum = points[0]
    for p in points:
        if(p < minimum):
            minimum = p
    for i in range(len(points)):
        if(points[i] == minimum):
            indices.append(i)
    return indices

#helper function to calculate the points
def cal_pts(rank):
    '''
    Given a rank, return the corresponding pts

    Parameters
    ----------
    rank : Int

    Returns
    -------
    Int
    
    >>> cal_pts(0)
    2
    >>> cal_pts(12)
    1
    >>> cal_pts(11)
    10
    '''
    two_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    jack_king = [9, 10, 11]
    
    if(rank in two_ten):
        return rank + 2
    elif(rank in jack_king):
        return 10
    elif(rank == 12):
        return 1

def calculate_round_points(hand):
    '''
    returns the point value of that hand.

    Parameters
    ----------
    hand : list

    Returns
    -------
    int

    >>> calculate_round_points([1, 2, 3, 4])
    8
    >>> calculate_round_points([49, 50, 51, 52]) 
    4
    '''
    pts = 0
    for card in hand:
        rank = card1.get_rank(card)
        pts += cal_pts(rank)
    return pts

def is_valid_group(cards):
    '''
    returns True if the cards form a valid group, and False otherwise.

    Parameters
    ----------
    cards : list

    Returns
    -------
    Boolean

    >>> is_valid_group([1, 2, 3]) 
    True
    >>> is_valid_group([1, 2, 3, 52]) 
    False
    '''
    
    if(len(cards) >= 3):
        return (card2.all_same_rank(cards))
    else:
        return False
    
def is_valid_sequence(cards):
    '''
    returns True if the cards form a valid sequence, and False otherwise.

    Parameters
    ----------
    cards : list

    Returns
    -------
    Boolean

    >>> is_valid_sequence([1, 5, 9]) 
    True
    >>> is_valid_sequence([1, 5, 10]) 
    False
    >>> is_valid_sequence([30, 34]) 
    False
    >>> is_valid_sequence([34, 38, 30]) 
    True
    '''
    result = True
    
    if(len(cards) >= 3):
        for i in range(1, len(cards)):
            result = result and ((cards[i] - cards[i-1]) % 4 == 0)
        return result
    else:
        return False

if __name__ == "__main__":
    doctest.testmod()
    