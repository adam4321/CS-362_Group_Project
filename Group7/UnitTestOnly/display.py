"""
Final Project CS-362
Oregon State University Winter term 2020
Group 7

Display class which renders the calculator's display
and calls the math operations in the operations.py file
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
            # "1": self.call_multiplication,
            # "2": self.call_division,
            # "3": self.call_square_root,
            # "4": self.call_power_two,
            # "5": self.call_inverse,
            # "6": self.call_factorial,
            # "7": self.call_absolute_val,
            # "8": self.call_sine,
            # "9": self.call_cosine,
            "0": self.call_exit
        }

        # Get the function from switcher dictionary
        self.current_operation = switcher.get(choice, lambda: "Invalid Operation")

    # Prompt for values and call multiplication function
    def call_multiplication(self):
        op1 = input("The first operand ")
        op2 = input("The second operand ")
        print()
        print(op1 + " * " + op2 + " = " + str(operations.multiplication(float(op1), float(op2))))

    # Prompt for values and call division function


    # Prompt for values and call power 2 function


    # Prompt for values and call square root function


    # Prompt for values and call inverse function


    # Prompt for values and call factorial function


    # Prompt for values and call absolute value function


    # Prompt for values and call sine function


    # Prompt for values and call cosine function


    # Print message and exit
    def call_exit(self):
        print("-- Goodbye --")
        self.exit = True
