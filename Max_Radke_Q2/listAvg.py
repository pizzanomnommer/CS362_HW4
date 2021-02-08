# Name: Max Radke   Date: Febuary 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 4
# Description: Takes a list of ints and calculates the average

def getAvg(List):
    # Make sure we got a list
    if not isinstance(List, list):
        raise TypeError
    
    # No empty lists, that would give a DBZ error
    if len(List) == 0:
        raise ZeroDivisionError

    # Check List content
    for x in List:
        # No strings, chars, ect, just ints
        if not isinstance(x, int):
            raise TypeError
    
    # Calculate average
    total = 0
    for x in List:
        total = total + x

    return total / len(List)