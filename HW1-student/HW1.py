# PIC 16A HW1
# Name: Palash Raval
# Collaborators: None
# Date: May 5, 2025

import random # This is only needed in Problem 5

# Problem 1

def print_s(s):
    ''' Prints a given string.
    Args:
        s: A string.
    Returns:
        None
    '''
    print(s)

# you do not have to add docstrings for the rest of these print_s_* functions.

def print_s_lines(s):
    new_s = s.split(":")
    for each in new_s:
        print(each.strip().strip())


def print_s_parts(s):
    for one_line in s.strip().split('\n'):
        first_word = one_line.split()[0]
        print(first_word)


def print_s_some(s):
    for tab_in_line in s.split('\n'):
        if "\t" in tab_in_line:
            print(tab_in_line)


def print_s_change(s):
    s = s.replace("math", "data science")
    s = s.replace("long division", "machine learning")
    print(s)


# Problem 2 

def make_count_dictionary(L):
    ''' 
    This function will give the counts of the unique elements within a provided list.
    The input for this function is L, which should be a list data type. This will be the list
    that you want the count information for each element about.
    The output for this function is D, which is a dictionary data type. This will provide you each unique value 
    within your list and the number of times this value is present in your provided list.
    '''
    D = {}
    list_as_set = set(L)

    for element in list_as_set:
        D[element] = L.count(element)    

    return(D)


# Problem 3

def gimme_an_odd_number():
    ''' 
    This function will continue to ask the user to input a number until an odd number is entered. 
    Once this happens, the function will provide the user with all the inputs that they entered until an odd number 
    was entered.
    The input for this function will be a string, whole number that will be converted into an integer.
    The output for this function will be a list that shows all of the inputs that the user made throughout the function call.
    '''
    number_input = int(input("Please enter an integer."))

    number_list = []
    while number_input % 2 == 0:
        number_list.append(number_input)
        number_input = int(input("Please enter an integer."))
    
    number_list.append(number_input)
    return(number_list)


# Problem 4

def get_triangular_numbers(k):
    ''' WRITE YOUR OWN DOCSTRING HERE
    '''
    pass # replace with your code


def get_consonants(s):
    ''' WRITE YOUR OWN DOCSTRING HERE
    '''
    pass # replace with your code


def get_list_of_powers(X, k):
    ''' WRITE YOUR OWN DOCSTRING HERE
    '''
    pass # replace with your code


def get_list_of_even_powers(L, k):
    ''' WRITE YOUR OWN DOCSTRING HERE
    '''
    pass # replace with your code



# Problem 5

def random_walk(ub, lb):
    ''' WRITE YOUR OWN DOCSTRING HERE
    '''
    pass # replace with your code


# If you uncomment these two lines, you can run 
# the gimme_an_odd_number() function by
# running this script on your IDE or terminal. 
# Of course you can run the function in notebook as well. 
# Make sure this stays commented when you submit
# your code.
#
# if __name__ == "__main__":
#     gimme_an_odd_number()
