#!/usr/bin/env python

from tkinter import font
from tkinter import *
import operations

class Window(Frame):

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master

        # self.pack(fill=BOTH, expand=1)
        self.grid(sticky=N+S+E+W)

        # maintain operators for multi operand functions
        self.firstOperand = None
        self.operator = None

        # input validation
        vcmd = (self.register(self.validate), '%P')
        # number read out field
        self.num1 = StringVar()
        self.displayField = Entry(self, textvariable=self.num1, validate='key', validatecommand=vcmd, justify=RIGHT)
        self.displayField.icursor(END)
        self.displayField.grid(row=0, column=0, rowspan=2, columnspan=25, ipadx=2, ipady=2, padx=5, pady=5, sticky=N+S+E+W)
        # number and function buttons
        calcButtons = ["sin", "cos", "|x|", "x!", "1/x", "7", "8", "9", "√x", "x^2",
                       "4", "5", "6", "-", "/", "1", "2", "3", "+", "*", "+/-", "0", ".", "C"]

        # create buttons
        i = 2
        j = 0
        for b in calcButtons:
            if j >= 25:
                j = 0
                i += 1
            button = Button(self, text=b, command=lambda m=b: self.doCallBack(m))
            button.grid(row=i, column=j, columnspan=5, sticky=N+S+E+W)
            j += 5
        
        equals = Button(self, text="=", bg='#76d76e', command=lambda m="=": self.doCallBack(m))
        equals.grid(row=6, column=20, columnspan=5, sticky=N+S+E+W)

    
    # validates input of entry field to float values
    def validate(self, value_if_allowed):
            if value_if_allowed:
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    self.bell()             # make fun error sound
                    return False
            else:
                self.bell()             # make fun error sound
                return False


    def clear(self):
        self.firstOperand = None
        self.operator = None
        return

    def setTwoOperator(self, op):
        self.firstOperand = float(self.displayField.get())
        self.operator = op
        self.num1.set('')
        print(f'{self.firstOperand}, {self.operator}')
        return

    # returns current value of entry field
    def doCallBack(self, method):
        inputButtons = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "."]
        number = self.displayField.get()
        if method in inputButtons:
            if number == "0":
                self.num1.set(method.strip('\"'))
                return
            else:
                number += method.strip('\"')
                if self.validate(number):
                    self.num1.set(number)
                return
        elif method == "C":
            self.num1.set('')
            self.clear()
            return
        elif method == "+/-":
            self.num1.set(str(0 - float(number)))
            return
        elif method == "+":
            self.setTwoOperator("+")
            return
        elif method == "-":
            self.setTwoOperator("-")
            return
        elif method == "*":
            self.setTwoOperator("*")
            return
        elif method == "/":
            self.setTwoOperator("/")
            return
        elif method == "sin":
            self.clear()
            self.num1.set(operations.sine(float(number)))
            return
        elif method == "cos":
            self.clear()
            self.num1.set(operations.cosine(float(number)))
            return
        elif method == "|x|":
            self.clear()
            self.num1.set(operations.absolute_val(float(number)))
            return
        elif method == "x!":
            self.clear()
            self.num1.set(operations.factorial(float(number)))
            return
        elif method == "1/x":
            self.clear()
            self.num1.set(operations.inverse(float(number)))
            return
        elif method == "√x":
            self.clear()
            self.num1.set(operations.square_root(float(number)))
            return
        elif method == "√x":
            self.clear()
            self.num1.set(operations.square_root(float(number)))
            return
        elif method == "x^2":
            self.clear()
            self.num1.set(operations.power_two(float(number)))
            return
        elif method == "=":
            if self.firstOperand != None:
                secondOperand = float(number)
                if self.operator == "+":
                    self.num1.set(self.firstOperand + secondOperand)
                    self.clear()
                    return
                elif self.operator == "-":
                    self.num1.set(self.firstOperand - secondOperand)
                    self.clear()
                    return
                elif self.operator == "*":
                    self.num1.set(operations.multiplication(self.firstOperand, secondOperand))
                    self.clear()
                    return
                elif self.operator == "/":
                    if secondOperand != 0:
                        self.num1.set(operations.division(self.firstOperand, secondOperand))
                        self.clear()
                        return
                    else:
                        self.bell()
                        return
            else:
                self.bell()
                return
        else:
            return


root = Tk()                             # declare tikinter UI
root.title("Simple Calculator")         # set display title
# root.geometry("500x500")              # optional fixed size
default_font = font.nametofont("TkDefaultFont")     # create font specification object (for sizing)
default_font.configure(size=24)                     # congifure font ob
root.option_add("*Font", default_font)              # set font ob to be used by our tkinter UI

app = Window(root)                      # create window object

root.mainloop()                         # run main
