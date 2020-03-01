"""
Final Project CS-362
Oregon State University Winter term 2020
Group 7

File that defines the display and calls the selected
math operation from operations.py
"""

import operations

class Display:
    def __init__(self):
        self.exit = False
        self.current_operation = None
        self.menu_string = ("\n"
            "   Command line Calculator     \n"
            "             --                \n"
            "(1) Multiplication\n"
            "(2) Division\n"
            "(3) Square_Root\n"
            "(4) Power_Two\n"
            "(5) Inverse\n"
            "(6) Factorial\n"
            "(7) Absolute_Val\n"
            "(8) Sine\n"
            "(9) Cosine\n"
            "\n"
            "(0) EXIT\n")
        
    # Menu printed in while loop until exit
    def print_menu(self):
        print(self.menu_string)

    # Receives keyboard input to set current function
    def choose_operation(self):
        choice = input("Which operation would you like?  ")
        print()

        switcher = {
            "1": self.call_multiplication,
            "2": self.call_division,
            "3": self.call_square_root,
            "4": self.call_power_two,
            "5": self.call_inverse,
            "6": self.call_factorial,
            "7": self.call_absolute_val,
            "8": self.call_sine,
            "9": self.call_cosine,
            "0": self.call_exit
        }

        # Get the function from switcher dictionary
        self.current_operation = switcher.get(choice, lambda: "Invalid Operation")
        
    # Prompt for values and call multiplication function
    def call_multiplication(self):
        op1 = input("The first operand? ")
        op2 = input("The second operand? ")
        print()
        try:
            print(op1 + " * " + op2 + " = " + str(operations.multiplication(float(op1), float(op2))))
        except:
            print("Invalid operand type")

    # Prompt for values and call division function
    def call_division(self):
        op1 = input("The dividend? ")
        op2 = input("The divisor? ")
        print()
        try:
            print(op1 + " / " + op2 + " = " + str(operations.division(float(op1), float(op2))))
        except:
            print("Invalid operand type")

    # Prompt for values and call power 2 function
    def call_square_root(self):
        op1 = input("The square root of? ")
        print()
        try:
            print("sqrt of " + op1 + " = " + str(operations.square_root(float(op1))))
        except:
            print("Invalid operand type")

    # Prompt for values and call square root function
    def call_power_two(self):
        op1 = input("The number to square? ")
        print()
        try:
            print(op1 + " ^ 2 = " + str(operations.power_two(float(op1))))
        except:
            print("Invalid operand type")

    # Prompt for values and call inverse function
    def call_inverse(self):
        op1 = input("The inverse of? ")
        print()
        try:
            print(op1 + " * 1/x = " + str(operations.inverse(float(op1))))
        except:
            print("Invalid operand type")

    # Prompt for values and call inverse function
    def call_factorial(self):
        op1 = input("The factorial of? ")
        print()
        try:
            print(op1 + "! = " + str(operations.factorial(float(op1))))
        except:
            print("Invalid operand type")

    # Prompt for values and call inverse function
    def call_absolute_val(self):
        op1 = input("The absolute value of? ")
        print()
        try:
            print("|" + op1 + "|" + " = " + str(operations.absolute_val(float(op1))))
        except:
            print("Invalid operand type")

    # Prompt for values and call inverse function
    def call_sine(self):
        op1 = input("The sine in radians of? ")
        print()
        try:
            print("sin" + op1 + " = " + str(operations.sine(float(op1))))
        except:
            print("Invalid operand type")

    # Prompt for values and call inverse function
    def call_cosine(self):
        op1 = input("The cosine in randians of? ")
        print()
        try:
            print("cos " + op1 + " = " + str(operations.cosine(float(op1))))
        except:
            print("Invalid operand type")

    # Print message and exit
    def call_exit(self):
        print("-- Goodbye --")
        self.exit = True
