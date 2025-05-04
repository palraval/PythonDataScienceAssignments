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
    The input for this function originally takes nothing. The user must simply call the function to which they will be
    prompted to enter a number. This number will be a string, whole number that will be converted into an integer.
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
    '''
    This function will provide a sum of all of the numbers leading up to the number the user has asked for.
    The input for this function is an integer, represented by k. 
    The output for this function is a list containing the sums of each of the values leading up to k and all its previous values.
    '''
    sum_list = [sum(list(range(1, number + 1))) for number in range(1, k + 1)]
    print(sum_list)



def get_consonants(s):
    ''' 
    This function will take in a string and provide all the characters inside this string
    that are not vowels, spaces, commas, and periods in the same order as the given string. 
    The input for this function is a string.
    The output for this function is a list.
    '''
    return [letter for letter in s if letter not in ["a", "e", "i", "o", "u", " ", ",", "."]]


def get_list_of_powers(X, k):
    '''
    This function has two inputs: a list of integer values (X) and an integer (k).
    This function will look at each element within the list X and exponentiate 
    with positive, integer values up to k. 
    It will then output a nested list, where each element of the list contains
    a list with the integer values of the powered X values. 
    '''
    return [[number ** power for power in range(k + 1)] for number in X]


def get_list_of_even_powers(L, k):
    ''' 
    This function has two inputs: a list of integer values (L) and an integer (k).
    This function will look at each element inside the list L and then exponentiate with
    an even, whole number from 0 to k. 
    It will then return a nested list, where each element of the list is a list 
    with the integer values for the even-powered L values. 
    '''
    return [[number ** power for power in range(k + 1) if power % 2 == 0] for number in L]



# Problem 5

def random_walk(lb, ub):
    ''' 
    This function will do a random walk based on the starting position of 0 and determine
    the direction of travel based on a coin flip (-1 for tails, 1 for heads). This will continue
    until either the upper or lower bound is reached.

    This function takes in two integers as the input (ub and lb).

    The output that is returned once the upper or lower bound is reached is: final position(pos) - integer,
    records of position throughout the walks (positions) - list, and records of the coin flip 
    travel directions (steps) - list.

    '''
    current_position = 0 
    positions = []
    steps = []

    while True:
        if current_position == lb:
            print(f"Lower bound at {lb} reached!")
            pos = current_position
            break

        elif current_position == ub:
            print(f"Upper bound at {ub} reached!")
            pos = current_position

            break    
        
        else:    
            positions.append(current_position)
            coin_toss = random.choice(['heads', 'tails'])
            if coin_toss == 'heads':
                steps.append(1)
                current_position = current_position + 1
            elif coin_toss == 'tails':
                steps.append(-1)
                current_position = current_position - 1
        
   
    return pos, positions, steps    


# If you uncomment these two lines, you can run 
# the gimme_an_odd_number() function by
# running this script on your IDE or terminal. 
# Of course you can run the function in notebook as well. 
# Make sure this stays commented when you submit
# your code.
#
# if __name__ == "__main__":
#     gimme_an_odd_number()
