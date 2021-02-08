# Name: Max Radke   Date: Febuary 7, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 4
# Description: Tests the file "cubeVolume.py"
#
# How to run: Open the directory that this file is in with command prompt.
#             Make sure that cubeVolume.py is in the same directory.
#             Type "python ./test_cubeVolume.py"

import unittest
import cubeVolume

class TestCubeVolume(unittest.TestCase):

    # three positive integers should pass
    def test1(self):
        result = cubeVolume.Calculate(10,10,10)
        self.assertEqual(result, 1000)

    # Any negative integers should fail
    def test2(self):
        with self.assertRaises(ValueError):
            cubeVolume.Calculate(-10,10,10)

    # Any input that is not an integer should fail
    def test3(self):
        with self.assertRaises(TypeError):
            cubeVolume.Calculate(10,"ten",10)

# call the tests
if __name__ == "__main__":
    unittest.main(verbosity=2)