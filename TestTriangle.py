# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_Equilateral_triangle(self):
        self.assertEqual(classifyTriangle(6,6,6), "Equilateral")

    def test_Isosceles_triangle(self):
        self.assertEqual(classifyTriangle(4,4,6), "Isosceles")

    def test_Scalene_triangle(self):
        self.assertEqual(classifyTriangle(6,3,9), "Scalene")

    def test_Right_triangle(self):
        self.assertEqual(classifyTriangle(3,4,5), "Scalene and Right")

    def test_If_triangle(self):
        self.assertEqual(classifyTriangle(0,4,5), "Not a triangle")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

