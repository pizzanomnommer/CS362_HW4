# Name: Max Radke   Date: Febuary 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 4
# Description: Tests file "listAvg.py"
#
# How to run: Open the directory that this file is in with command prompt.
#             Make sure that listAvg.py is in the same directory.
#             Type "python ./test_listAvg.py"

import unittest
import listAvg

class TestListAvg(unittest.TestCase):
    # Test an average with an integer result
    def test1(self):
        result = listAvg.getAvg([1,2,3,4,5])
        self.assertEqual(result, 3)

    # Test an average with a float result
    def test2(self):
        result = listAvg.getAvg([1,2,3,4,5,6])
        self.assertEqual(result, 3.5)

    # Test that it only accepts lists
    def test3(self):
        with self.assertRaises(TypeError):
            listAvg.getAvg(1)

    # Test empty lists
    def test4(self):
        with self.assertRaises(ZeroDivisionError):
            listAvg.getAvg([])

# call the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)
