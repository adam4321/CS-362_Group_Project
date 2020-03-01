"""
Final Project CS-362
Oregon State University Winter term 2020
Group 7

Entry point for calculator
"""

import display

def main():
    # Create a display instance
    running_calc = display.Display()

    # Loop until the user chooses to exit (0 on menu) 
    while running_calc.exit == False:
        running_calc.print_menu()
        running_calc.choose_operation()
        running_calc.current_operation()

        if (running_calc.exit == True):
            break


# Define this file as main
if __name__ == '__main__':
    main()