# Name: Max Radke   Date: Febuary 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 4
# Description: Tests the file "fullName.py"
#
# How to run: Open the directory that this file is in with command prompt.
#             Make sure that cubeVolume.py is in the same directory.
#             Type "python ./test_cubeVolume.py"

import unittest
from unittest import result
import fullName

class TestFullName(unittest.TestCase):

    # Two strings should pass
    def test1(self):
        result = fullName.getName("Max", "Radke")
        self.assertEqual(result, "Max Radke")

    # An input of an int should fail
    def test2(self):
        with self.assertRaises(TypeError):
            fullName.getName(22, "Radke")

    # If either of the strings have a space, it is
    # not only a first/last name and should fail
    def test3(self):
        with self.assertRaises(NameError):
            fullName.getName("Max Ervin", "Radke")

# call the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)