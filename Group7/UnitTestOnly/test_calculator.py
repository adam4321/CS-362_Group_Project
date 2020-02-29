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
        test_val1 = operations.multiplication(5, 6)
        test_val2 = operations.multiplication(-5, 6)
        test_val3 = operations.multiplication(5.3, 6.7)

        assert(test_val1 == 30)
        assert(test_val2 == -30)
        assert(test_val3 == 35.51)

    def test_division(self):
        test_val1 = operations.division(4, 2)
        test_val2 = operations.division(5, -2)
        test_val3 = operations.division(5.8, 2.5)
        test_val4 = operations.division(5.3, 6.7)

        assert(test_val1 == 2)
        assert(test_val2 == -2.5)
        assert(test_val3 == 2.32)
        assert(test_val4 == 0.791045)

    def test_square_root(self):
        test_val1 = operations.square_root(16)
        test_val2 = operations.square_root(4)
        test_val3 = operations.square_root(64)
        test_val4 = operations.square_root(73.96)

        assert(test_val1 == 4)
        assert(test_val2 == 2)
        assert(test_val3 == 8)
        assert(test_val4 == 8.6)

    def test_power_two(self):
        test_val1 = operations.power_two(4)
        test_val2 = operations.power_two(-2)
        test_val3 = operations.power_two(8)
        test_val4 = operations.power_two(8.6)

        assert(test_val1 == 16)
        assert(test_val2 == 4)
        assert(test_val3 == 64)
        assert(test_val4 == 73.96)

    def test_inverse(self):
        test_val1 = operations.inverse(4)
        test_val2 = operations.inverse(-2)
        test_val3 = operations.inverse(8)
        test_val4 = operations.inverse(8.6)

        assert(test_val1 == 0.25)
        assert(test_val2 == -0.5)
        assert(test_val3 == 0.125)
        assert(test_val4 == 0.116279)

    def test_factorial(self):
        test_val1 = operations.factorial(-1)
        test_val2 = operations.factorial(0)
        test_val3 = operations.factorial(1)
        test_val4 = operations.factorial(5)

        assert(test_val1 == "Invalid Input")
        assert(test_val2 == 1)
        assert(test_val3 == 1)
        assert(test_val4 == 120)

    def test_absolute_val(self):
        test_val1 = operations.absolute_val(-1)
        test_val2 = operations.absolute_val(0)
        test_val3 = operations.absolute_val(1)
        test_val4 = operations.absolute_val(-5.5)

        assert(test_val1 == 1)
        assert(test_val2 == 0)
        assert(test_val3 == 1)
        assert(test_val4 == 5.5)

    def test_sine(self):
        test_val1 = operations.sine(1)
        test_val2 = operations.sine(0)
        test_val3 = operations.sine(1.5)
        test_val4 = operations.sine(2.58)

        assert(test_val1 == 0.841471)
        assert(test_val2 == 0)
        assert(test_val3 == 0.997495)
        assert(test_val4 == 0.532535)

    def test_cosine(self):
        test_val1 = operations.cosine(1)
        test_val2 = operations.cosine(0)
        test_val3 = operations.cosine(1.5)
        test_val4 = operations.cosine(2.58)

        assert(test_val1 == 0.540302)
        assert(test_val2 == 1)
        assert(test_val3 == 0.070737)
        assert(test_val4 == -0.846408)
