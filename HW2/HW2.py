# HW2
# Name: Palash Raval
# Collaborators: None
# Date: May 12, 2025

import random

def count_characters(s):
    """
    This function will return the count of each character that appears in the string it is given.
    The input for this function is a string, denoted by s.
    The output for this function is a dictionary called letter_counter.
    """
    letter_counter = {}
    for i in range(len(s)):
        if s[i] in letter_counter.keys():
            letter_counter[s[i]] += 1
        else:
            letter_counter[s[i]] = 1

    return letter_counter



def count_ngrams(s, n):
    """WRITE DOCSTRING HERE
    """
    pass # replace with your code


def markov_text(s, n, length, seed):
    """WRITE DOCSTRING HERE
    """
    pass # replace with your code
