#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    output  = []

    for num in range(n + 1):
        if num % 2 == 0:
            output += [num]

    return output