"""
Final Project CS-362
Oregon State University Winter term 2020
Group 7

Unit test file for the display.py and operations.py
"""


import calculator
import unittest
from unittest import TestCase
import pytest


class Test_Operations(TestCase):
    # Test valid input vs output for each math operation
    def test_multiplication(self):
        test_val1 = calculator.multiplication(5, 6)
        test_val2 = calculator.multiplication(-5, 6)
        test_val3 = calculator.multiplication(5.3, 6.7)

        self.assertTrue(test_val1, 30)
        self.assertTrue(test_val2, -30)
        self.assertTrue(test_val3, 35.51)

    def test_division(self):
        test_val1 = calculator.division(4, 2)
        test_val2 = calculator.division(5, -2)
        test_val3 = calculator.division(5.8, 2.5)
        test_val4 = calculator.division(5.3, 6.7)

        self.assertTrue(test_val1, 2)
        self.assertTrue(test_val2, -2.5)
        self.assertTrue(test_val3, 2.32)
        self.assertTrue(test_val4, 0.791045)

    def test_square_root(self):
        test_val1 = calculator.square_root(16)
        test_val2 = calculator.square_root(4)
        test_val3 = calculator.square_root(64)
        test_val4 = calculator.square_root(73.96)

        self.assertTrue(test_val1, 4)
        self.assertTrue(test_val2, 2)
        self.assertTrue(test_val3, 8)
        self.assertTrue(test_val4, 8.6)
        self.assertAlmostEqual(2,  calculator.square_root(5), 2)

    def test_power_two(self):
        test_val1 = calculator.power_two(4)
        test_val2 = calculator.power_two(-2)
        test_val3 = calculator.power_two(8)
        test_val4 = calculator.power_two(8.6)

        self.assertTrue(test_val1, 16)
        self.assertTrue(test_val2, 4)
        self.assertTrue(test_val3, 64)
        self.assertTrue(test_val4, 73.96)

    def test_inverse(self):
        test_val1 = calculator.inverse(4)
        test_val2 = calculator.inverse(-2)
        test_val3 = calculator.inverse(8)
        test_val4 = calculator.inverse(8.6)

        self.assertTrue(test_val1, 0.25)
        self.assertTrue(test_val2, -0.5)
        self.assertTrue(test_val3, 0.125)
        self.assertTrue(test_val4, 0.116279)

    def test_factorial(self):
        test_val1 = calculator.factorial(-1)
        test_val2 = calculator.factorial(0)
        test_val3 = calculator.factorial(1)
        test_val4 = calculator.factorial(5)

        self.assertTrue(test_val1, "Invalid Input")
        self.assertTrue(test_val2, 1)
        self.assertTrue(test_val3, 1)
        self.assertTrue(test_val4, 120)
        self.assertAlmostEqual(1,  calculator.factorial(1.2), 2)

    def test_absolute_val(self):
        test_val1 = calculator.absolute_val(-1)
        test_val2 = calculator.absolute_val(0)
        test_val3 = calculator.absolute_val(1)
        test_val4 = calculator.absolute_val(-5.5)

        self.assertTrue(test_val1, 1)
        self.assertTrue(test_val2, 0)
        self.assertTrue(test_val3, 1)
        self.assertTrue(test_val4, 5.5)

    def test_sine(self):
        test_val1 = calculator.sine(1)
        test_val2 = calculator.sine(0)
        test_val3 = calculator.sine(1.5)
        test_val4 = calculator.sine(2.58)

        self.assertTrue(test_val1, 0.841471)
        self.assertTrue(test_val2, 0)
        self.assertTrue(test_val3, 0.997495)
        self.assertTrue(test_val4, 0.532535)

    def test_cosine(self):
        test_val1 = calculator.cosine(1)
        test_val2 = calculator.cosine(0)
        test_val3 = calculator.cosine(1.5)
        test_val4 = calculator.cosine(2.58)

        self.assertAlmostEqual(test_val1, 540302, 5)
        self.assertTrue(test_val2, 1)
        self.assertTrue(test_val3, 0.070737)
        self.assertTrue(test_val4, -0.846408)
