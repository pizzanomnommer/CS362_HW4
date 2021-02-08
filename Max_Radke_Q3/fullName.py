# Name: Max Radke   Date: Febuary 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 4
# Description: Takes two name strings and returns a full name

def getName(str1, str2):
    # Make sure there is only one name in each
    if ' ' in str1 or ' ' in str2:
        raise NameError

    str1 = str1 + " " # Add a space
    return str1 + str2 # Return full name