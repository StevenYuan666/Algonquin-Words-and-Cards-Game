#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:34:18 2020

@author: stevenyuan
"""
import doctest

#declare the global variables
CONSONANTS = "bcdghkmnpstwyzj"
VOWELS = "aeio"
VOWELS_WITH_ACCENT = "àèìò"
PUNCTUATION = ',;:.?!-'
DIPHTHONGS = ['aw', 'ay', 'ew', 'ey', 'iw', 'ow']

def is_valid_consonant(c):
    '''
    Determine if a single character is a consonants

    Parameters
    ----------
    c : Char

    Returns
    -------
    Boolean

    >>> is_valid_consonant('j') 
    True
    >>> is_valid_consonant('l') 
    False
    >>> is_valid_consonant('G') 
    True
    '''
    if(len(c) == 1):
        lower = c.lower()
        return (lower in  CONSONANTS)
    else:
        return False

def is_valid_vowel(c):
    '''
    Determine if a single character is a vowel

    Parameters
    ----------
    c : Char

    Returns
    -------
    Boolean

    >>> is_valid_vowel('a') 
    True
    >>> is_valid_vowel('ai') 
    False
    >>> is_valid_vowel('h') 
    False
    '''
    if(len(c) == 1):
        lower = c.lower()
        return ((lower in  VOWELS) or (lower in VOWELS_WITH_ACCENT))
    else:
        return False
    
def is_valid_single_word(w):
    '''
    Check if w is a valid algonquin word

    Parameters
    ----------
    w : String
    
    Returns
    -------
    Boolean

    >>> is_valid_single_word('Kwey') 
    True
    >>> is_valid_single_word('rats') 
    False
    >>> is_valid_single_word('ay,dj') 
    False
    '''
    
    result = True
    for c in w:
        result = result and (is_valid_consonant(c) or is_valid_vowel(c))
    return result

def is_valid_phrase(s):
    '''
    Check if s is a valid phrase

    Parameters
    ----------
    s : String

    Returns
    -------
    Boolean

    >>> is_valid_phrase('Kwey') # Hello
    True
    >>> is_valid_phrase('Andi ejayan?') # Where are you going?
    True
    >>> is_valid_phrase('I scream, you scream, we all scream for ice cream') 
    False
    '''
    
    result = True
    for c in s:
        result = result and (is_valid_consonant(c) or is_valid_vowel(c) or (c == " ") or (c in PUNCTUATION))
    return result
    
if __name__ == "__main__":
    doctest.testmod()