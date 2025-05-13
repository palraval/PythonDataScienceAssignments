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



def count_ngrams(s, n = 1):
    """
    This function will provide the counts of each chunk in a string, with each chunk being determined by the user.
    There are two inputs for this function: a string(s) and an integer(n).
    The output of this function will be a dictionary called ngram_counter that shows how many times each unique chunk
    is present in a string.
    """
    ngram_counter = {}

    for i in range(len(s)):
        if (s[i:i + n] in ngram_counter.keys()) & (len(s[i:i + n]) == n):
                ngram_counter[s[i: i + n]] += 1
    
        elif (s[i:i + n] not in ngram_counter.keys()) & (len(s[i:i + n]) == n):
            ngram_counter[s[i: i + n]] = 1
            
    return ngram_counter



def markov_text(s, n, length = 100, seed = "Emma Woodhouse"):
    """
    This function will generate new text starting with a provided string(seed). It will look at all the
    chunks based on a string (s) and store the chunks that begin with the final three characters of seed.
    It will create a dictionary of occurences for each chunk and use that to determine the respective weights.
    This function will then randomly select one of these chunks and then add the final character in this string
    to the end of the seed string. It will continue looping through this until the length specified is reached plus
    the length of the seed.
    There are four inputs for this function: a string (s), an integer (n), an integer (length), and a string (seed).
    The output for this function will be a string that begins with the seed plus the generated characters that reach
    the specified length.
    """
    check_start_dictionary = count_ngrams(s, n + 1)
    start_string = seed

    while len(start_string) - len(seed) < length:

        ending_string = start_string[-n:]
        storage_list = []
        storage_dictionary = {}

        for key in check_start_dictionary.keys():
            if key.startswith(ending_string):
                storage_list.append(key)

        
        for element in storage_list:
            storage_dictionary[element] = check_start_dictionary[element]


        weights_list = []
        for value in storage_dictionary.values():
            weights_list.append(value/sum(storage_dictionary.values()))


        new_string = random.choices(list(storage_dictionary.keys()), weights_list)[0]

        start_string = start_string + new_string[-1]

    return(start_string)

