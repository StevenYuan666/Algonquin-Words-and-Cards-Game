#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:01:58 2020

@author: stevenyuan
"""

import doctest
import algonquin_utils as utils

def get_consonant_pronunciation(c):
    '''
    Return the pronunciation of a valid character

    Parameters
    ----------
    c : Char

    Returns
    -------
    String
    
    >>> get_consonant_pronunciation('d') 
    'D'
    >>> get_consonant_pronunciation('j') 
    'GE'
    >>> get_consonant_pronunciation('r')
    ''
    '''
    
    char = c.upper()
    if(utils.is_valid_consonant(char)):
        if(char == "J"):
            return "GE"
        else:
            return char
    else:
        if (char == "DJ"):
            return "J"
        else:
            return ""
    
def get_vowel_pronunciation(c):
    '''
    Return the pronunciation of a valid vowel

    Parameters
    ----------
    c : Char

    Returns
    -------
    String
    
    >>> get_vowel_pronunciation("a") 
    'A'
    >>> get_vowel_pronunciation("è") 
    'E'
    >>> get_vowel_pronunciation("o") 
    'U'
    '''
    
    char = c.lower()
    if(utils.is_valid_vowel(char)):
        if(char in 'aà'):
            return 'A'
        elif(char in 'eè'):
            return 'E'
        elif(char == 'i'):
            return 'I'
        elif(char == 'ì'):
            return 'EE'
        elif(char == 'o'):
            return 'U'
        elif(char == 'ò'):
            return 'O'
    else:
        return ''
    
def get_diphthong_pronunciation(c):
    '''
    Return the pronunciation of a diphthong

    Parameters
    ----------
    c : String

    Returns
    -------
    String

    >>> get_diphthong_pronunciation("ay") 
    'EYE'
    >>> get_diphthong_pronunciation("ow") 
    'OW'
    >>> get_diphthong_pronunciation("oy") 
    ''
    '''
    
    char = c.lower()
    if(char in utils.DIPHTHONGS):
        if (char in ['aw', 'ow']):
            return 'OW'
        elif(char == 'ay'):
            return 'EYE'
        elif(char == 'ew'):
            return 'AO'
        elif(char == 'ey'):
            return 'AY'
        elif(char == 'iw'):
            return 'EW'
    else:
        return ''
    
def get_word_pronunciation(w):
    '''
    Return the pronunciation of a valid word

    Parameters
    ----------
    w : String

    Returns
    -------
    String

    >>> get_word_pronunciation('kwey') # hello
    'KWAY'
    >>> get_word_pronunciation('madjashin') # see you later 
    'MAJASHIN'
    >>> get_word_pronunciation('kasagiyan') # i love you 
    'KASAGIYAN'
    '''
    pro = ''
    word = w.lower()
    index_pointer = -1
    if(utils.is_valid_single_word(word)):
        for i in range(len(word)):
            if(index_pointer != i):
                if(i != (len(word) - 1)):
                    chars = word[i] + word[i+1]
                else:
                    chars = word[i]
                c = word[i]
                if(chars in utils.DIPHTHONGS):
                    pro += get_diphthong_pronunciation(chars)
                    index_pointer = i + 1
                elif(chars == 'dj'):
                    pro += 'J'
                    index_pointer = i + 1
                elif(utils.is_valid_consonant(c)):
                    pro += get_consonant_pronunciation(c)
                elif(utils.is_valid_vowel(c)):
                    pro += get_vowel_pronunciation(c)
    return pro

def tokenize_sentence(s):
    '''
    given a string, if it is a valid phrase break it down into strings 
    representing either single words or a sequence of punctuation marks 
    and space characters.

    Parameters
    ----------
    s : String

    Returns
    -------
    list


    >>> tokenize_sentence("a test")
    ['a', ' ', 'test']
    >>> tokenize_sentence("just__@a# test!")
    []
    >>> tokenize_sentence('Kwey') # Hello
    ['Kwey']
    >>> tokenize_sentence('Kwey, anin eji-pimadizin?') # Hello, how are you? 
    ['Kwey', ', ', 'anin', ' ', 'eji', '-', 'pimadizin', '?']
    '''
    result = []
    tmp = ''
    if(utils.is_valid_phrase(s)):
        for i in range(len(s)):
            c = s[i]
            if((c in utils.PUNCTUATION) or c == " "):
                if (i != 0 and not ((s[i-1] in utils.PUNCTUATION) or s[i-1] == " ")):
                    result.append(tmp)
                    tmp = ""
                    tmp += c
                else:
                    tmp += c
            else:
                if ((i != 0) and (s[i-1] in utils.PUNCTUATION) or s[i-1] == " "):
                    result.append(tmp)
                    tmp = ""
                    tmp += c
                else:
                    tmp += c
            if(i == len(s) - 1):
                result.append(tmp)
    return result
                
def get_sentence_pronunciation(s):
    '''
    given a string, if it is a valid string return its pronunciation, 
    otherwise return an empty string.

    Parameters
    ----------
    s : String

    Returns
    -------
    list

    >>> get_sentence_pronunciation('Kwey') # Hello
    'KWAY'
    >>> get_sentence_pronunciation('Andi ejayan?') # Where are you going?
    'ANDI EGEEYEAN?'
    >>> get_sentence_pronunciation('Mino ishkwa nawakwe') # Good afternoon
    'MINU ISHKWA NOWAKWE'
    >>> get_sentence_pronunciation("I scream, you scream, we all scream for ice cream") 
    ''
    '''
    
    list_sentence = tokenize_sentence(s)
    pro = ''
    for word in list_sentence:
        if(utils.is_valid_single_word(word)):
            pro += get_word_pronunciation(word)
        else:
            pro += word
    return pro
    
if __name__ == "__main__":
    doctest.testmod()