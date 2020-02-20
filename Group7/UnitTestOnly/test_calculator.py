"""
Group 7 Final Project CS-362
Oregon State University Winter term 2020

"""

import calculator
from unittest import TestCase


class Test_Calculator(TestCase):
    def set_up(self):
        self.message = "hello world"

    def test_init(self):
        self.set_up()

    def test_Multiplication(self):
        self.set_up()

    def test_Division(self):
        self.set_up()

    def test_Square_Root(self):
        self.set_up()

    def test_Power_Two(self):
        self.set_up()

    def test_Inverse(self):
        self.set_up()

    def test_Factorial(self):
        self.set_up()

    def test_Absolue_Val(self):
        self.set_up()

    def test_Sine(self):
        self.set_up()

    def test_Cosine(self):
        self.set_up()

# Calculator test instance
test_calc = calculator.Calc("hello world")
print('\n' + test_calc.message)