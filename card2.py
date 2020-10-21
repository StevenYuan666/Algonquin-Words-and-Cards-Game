#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:10:46 2020

@author: stevenyuan
"""

import doctest
import card1
#declare the global variable
SUITS = [0, 1, 2, 3]
RANKS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
SUITS_STR = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS_STR = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', \
             'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    
def get_card(suit, rank):
    '''
    returns the integer representation of the card with that suit and rank

    Parameters
    ----------
    suit : String
    rank : String

    Returns
    -------
    Int

    >>> get_card(0, 0)
    1
    >>> get_card(0, 1)
    5
    >>> get_card(3, 12) # Ace of Spades 
    52
    '''
    result = rank * 4 + (suit + 1)
    return result

def card_to_string(card):
    '''
    returns a string for that card’s name in the form RANK of SUIT

    Parameters
    ----------
    card : Int

    Returns
    -------
    String

    >>> card_to_string(1) 
    'TWO of HEARTS'
    >>> card_to_string(5) 
    'THREE of HEARTS'
    >>> card_to_string(52) 
    'ACE of SPADES'
    '''
    suit_index = card1.get_suit(card)
    rank_index = card1.get_rank(card)
    
    suit = SUITS_STR[suit_index]
    rank = RANKS_STR[rank_index]
    result = rank.upper() + ' of ' + suit.upper()
    
    return result

def hand_to_string(hand):
    '''
    returns a string containing the names of all the cards

    Parameters
    ----------
    hand : list

    Returns
    -------
    String

    >>> hand_to_string([1, 2, 3, 4])
    'TWO of HEARTS, TWO of DIAMONDS, TWO of CLUBS, TWO of SPADES'
    >>> hand_to_string([52]) 
    'ACE of SPADES'
    '''
    result = ""
    for i in range(len(hand)):
        if(i != len(hand) - 1):
            result += card_to_string(hand[i]) + ", "
        else:
            result += card_to_string(hand[i])
    return result

def get_deck():
    '''
    returns a list of integers containing the 52 cards in a deck of playing cards

    Returns
    -------
    list

    >>> deck = get_deck() 
    >>> len(deck)
    52
    '''
    deck = []
    for i in range(52):
        deck.append((i+1))
    return deck

def all_same_suit(cards):
    '''
    returns True if all cards in the list are of the same suit, and False otherwise.

    Parameters
    ----------
    cards : list

    Returns
    -------
    Boolean
    
    >>> all_same_suit([4, 52])
    True
    >>> all_same_suit([1, 2, 3, 4]) 
    False
    '''
    c1 = cards[0]
    for i in range(1,len(cards)):
        if not (card1.same_suit(c1, cards[i])):
            return False
    return True

def all_same_rank(cards):
    '''
    returns True if all cards in the list are of the same rank, and False otherwise.

    Parameters
    ----------
    cards : list

    Returns
    -------
    Boolean

    >>> all_same_rank([4, 52]) 
    False
    >>> all_same_rank([1, 2, 3, 4]) 
    True
    '''
    c1 = cards[0]
    for i in range(1,len(cards)):
        if not (card1.same_rank(c1, cards[i])):
            return False
    return True
    
if __name__ == "__main__":
    doctest.testmod()