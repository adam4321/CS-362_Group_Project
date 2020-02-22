"""
Final Project CS-362
Oregon State University Winter term 2020
Group 7

Unit testing file for the display.py and operations.py files
"""

import operations
import display
from unittest import TestCase


class Test_Operations(TestCase):
    def test_Multiplication(self):
        test_val1 = operations.Multiplication(5, 6)
        test_val2 = operations.Multiplication(-5, 6)
        test_val3 = operations.Multiplication(5.3, 6.7)


        assert(test_val1 == 30)
        assert(test_val2 == -30)
        assert(test_val3 == 35.51)

    def test_Division(self):
        test_val1 = operations.Division(4, 2)
        test_val2 = operations.Division(5, -2)
        test_val3 = operations.Division(5.8, 2.5)
        test_val4 = operations.Division(5.3, 6.7)

        assert(test_val1 == 2)
        assert(test_val2 == -2.5)
        assert(test_val3 == 2.32)
        assert(test_val4 == 0.791045)

    def test_Square_Root(self):
        test_val1 = operations.Square_Root(16)
        test_val2 = operations.Square_Root(4)
        test_val3 = operations.Square_Root(64)
        test_val4 = operations.Square_Root(73.96)

        assert(test_val1 == 4)
        assert(test_val2 == 2)
        assert(test_val3 == 8)
        assert(test_val4 == 8.6)

    def test_Power_Two(self):
        test_val1 = operations.Power_Two(4)
        test_val2 = operations.Power_Two(-2)
        test_val3 = operations.Power_Two(8)
        test_val4 = operations.Power_Two(8.6)

        assert(test_val1 == 16)
        assert(test_val2 == 4)
        assert(test_val3 == 64)
        assert(test_val4 == 73.96)

    def test_Inverse(self):
        test_val1 = operations.Inverse(4)
        test_val2 = operations.Inverse(-2)
        test_val3 = operations.Inverse(8)
        test_val4 = operations.Inverse(8.6)

        assert(test_val1 == 0.25)
        assert(test_val2 == -0.5)
        assert(test_val3 == 0.125)
        assert(test_val4 == 0.116279)

    # def test_Factorial(self):


    # def test_Absolute_Val(self):


    # def test_Sine(self):
        

    # def test_Cosine(self):


class Test_Display(TestCase):
    def set_up(self):
        self.exit = False
        self.current_operation = None

    def test_init(self):
        self.set_up()

        assert(self.exit == False)
        assert(self.current_operation == None)

    def test_Print_Menu(self):
        self.set_up()



    def test_Set_Exit(self):
        self.set_up()



    def test_Choose_Operation(self):
        self.set_up()


        