#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:53:31 2020

@author: stevenyuan
"""
import doctest
import card2

def draw(hand, top_discard_card):
    '''
    draw(hand, top_discard_card):

    Parameters
    ----------
    hand : list
    top_discard_card : Int

    Returns
    -------
    String

    >>> import human_player
    >>> location = human_player.draw([4, 50, 15, 21], 5)  #input 'stock'
    >>> print(location)
    stock
    >>> location = human_player.draw([4, 50, 15, 21], 5)  #input 'discard'
    >>> print(location)
    discard
    '''
    location = input('Draw location: ')
    return location

def discard(hand):
    '''
    Takes a list of the cards in the player’s hand as argument. 
    Prints out each card and its index in the list. 
    Asks the user to enter one of the indices, and returns the card at that index.

    Parameters
    ----------
    hand : list

    Returns
    -------
    Int

    >>> import human_player
    >>> card_to_discard = human_player.discard([4, 50, 15, 21]) #input Choice: 2
    0          TWO of SPADES
    1          ACE of DIAMONDS
    2          FIVE of CLUBS
    3          SEVEN of HEARTS
    >>> print(card_to_discard) 
    15
    '''
    for i in range(len(hand)):
        print(str(i) + '          ' + card2.card_to_string(hand[i]))
    choice = input('Choice: ')
    return hand[int(choice)]
    
if __name__ == '__main__':
    #doctest.testmod()
    choice = discard([4, 50, 15, 21])
    print(choice)
    
    