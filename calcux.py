#!/usr/bin/env python

from tkinter import font
from tkinter import *

class Window(Frame):

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master

        font
        # self.pack(fill=BOTH, expand=1)
        self.grid(sticky=W+E+N+S)

        # number read out field
        self.displayField = Entry(self, justify=RIGHT)
        self.displayField.insert(END, '')
        self.displayField.grid(row=0, column=0, rowspan=2, columnspan=6, ipadx=2, ipady=2, padx=5, pady=5, sticky=N+S+E+W)

        # number and function buttons
        # row 2
        sine = Button(self, text="sin", command=self.getEntry)
        sine.grid(row=2, column=0, columnspan=2, sticky=N+S+E+W)

        cosine = Button(self, text="cos", command=self.getEntry)
        cosine.grid(row=2, column=2, columnspan=2, sticky=N+S+E+W)

        absolute = Button(self, text="|x|", command=self.getEntry)
        absolute.grid(row=2, column=4, sticky=N+S+E+W)

        # row 3
        seven = Button(self, text="7", command=self.getEntry)
        seven.grid(row=3, column=0, sticky=N+S+E+W)

        eight = Button(self, text="8", command=self.getEntry)
        eight.grid(row=3, column=1, sticky=N+S+E+W)

        nine = Button(self, text="9", command=self.getEntry)
        nine.grid(row=3, column=2, sticky=N+S+E+W)

        divide = Button(self, text="/", command=self.getEntry)
        divide.grid(row=3, column=3, sticky=N+S+E+W)

        square = Button(self, text="x^2", command=self.getEntry)
        square.grid(row=3, column=4, sticky=N+S+E+W)

        # row 4
        four = Button(self, text="4", command=self.getEntry)
        four.grid(row=4, column=0, sticky=N+S+E+W)

        five = Button(self, text="5", command=self.getEntry)
        five.grid(row=4, column=1, sticky=N+S+E+W)

        six = Button(self, text="6", command=self.getEntry)
        six.grid(row=4, column=2, sticky=N+S+E+W)

        multiply = Button(self, text="*", command=self.getEntry)
        multiply.grid(row=4, column=3, sticky=N+S+E+W)

        inverse = Button(self, text="1/x", command=self.getEntry)
        inverse.grid(row=4, column=4, sticky=N+S+E+W)

        # row 5
        one = Button(self, text="1", command=self.getEntry)
        one.grid(row=5, column=0, sticky=N+S+E+W)

        two = Button(self, text="2", command=self.getEntry)
        two.grid(row=5, column=1, sticky=N+S+E+W)

        three = Button(self, text="3", command=self.getEntry)
        three.grid(row=5, column=2, sticky=N+S+E+W)

        subtract = Button(self, text="-", command=self.getEntry)
        subtract.grid(row=5, column=3, sticky=N+S+E+W)

        factorial = Button(self, text="x!", command=self.getEntry)
        factorial.grid(row=5, column=4, sticky=N+S+E+W)

        # row 6
        signed = Button(self, text="+/-", command=self.getEntry)
        signed.grid(row=6, column=0, sticky=N+S+E+W)

        zero = Button(self, text="0", command=self.getEntry)
        zero.grid(row=6, column=1, sticky=N+S+E+W)

        decimal = Button(self, text=".", command=self.getEntry)
        decimal.grid(row=6, column=2, sticky=N+S+E+W)

        add = Button(self, text="+", command=self.getEntry)
        add.grid(row=6, column=3, sticky=N+S+E+W)

        equals = Button(self, text="=", command=self.getEntry)
        equals.grid(row=6, column=4, sticky=N+S+E+W)


    def getEntry(self):
        number = float(self.displayField.get())
        print(f'displayField: {number}')


root = Tk()
root.title("Simple Calculator")
# root.geometry("500x500")
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=24)
root.option_add("*Font", default_font)

app = Window(root)

root.mainloop()
