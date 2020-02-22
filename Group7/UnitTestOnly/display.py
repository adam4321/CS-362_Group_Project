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
        
    # Menu printed in while loop until exit
    def Print_Menu(self):
        print()
        print("   Command line Calculator     ")
        print("             --                ")
        print("(1) Multiplication")
        print("(2) Division")
        print("(3) Square_Root")
        print("(4) Power_Two")
        print("(5) Inverse")
        print("(6) Factorial")
        print("(7) Absolute_Val")
        print("(8) Sine")
        print("(9) Cosine")
        print()
        print("(0) EXIT")
        print()

    # Receives keyboard input to set current function
    def Choose_Operation(self):
        choice = input("Which operation would you like?  ")
        print()

        switcher = {
            # "1": self.Call_Multiplication,
            # "2": self.Call_Division,
            # "3": self.Call_Square_Root,
            # "4": self.Call_Power_Two,
            # "5": self.Call_Inverse,
            # "6": self.Call_Factorial,
            # "7": self.Call_Absolute_Val,
            # "8": self.Call_Sine,
            # "9": self.Call_Cosine,
            "0": self.Call_Exit
        }

        # Get the function from switcher dictionary
        self.current_operation = switcher.get(choice, lambda: "Invalid Operation")

    # Prompt for values and call Multiplication Function
    def Call_Multiplication(self):
        op1 = input("The first operand ")
        op2 = input("The second operand ")
        print()
        print(op1 + " * " + op2 + " = " + str(operations.Multiplication(float(op1), float(op2))))

    # Prompt for values and call Multiplication Function


    # Prompt for values and call Power 2 Function


    # Prompt for values and call Square Root Function


    # Prompt for values and call Inverse Function


    # Prompt for values and call Factorial Function


    # Prompt for values and call Absolute Value Function


    # Prompt for values and call Sine Function


    # Prompt for values and call Cosine Function


    # Print message and exit
    def Call_Exit(self):
        print("-- Goodbye --")
        self.exit = True


def main():
    # Create a operations instance
    operations = Display()

    # Print menu and loop until exit
    while operations.exit == False:
        operations.Print_Menu()
        operations.Choose_Operation()
        operations.current_operation()

        if (operations.exit == True):
            break


if __name__ == '__main__':
    main()