# Name: Max Radke   Date: Febuary 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 4
# Description: Takes three inputs and calcuates the volume of a cube

def Calculate(x, y, z):
    # Make sure the input is not negative
    if x < 0 or y < 0 or z < 0:
        raise ValueError
    
    # Make sure input is an integer
    if not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int):
        raise TypeError

    # Return volume
    return x * y * z
