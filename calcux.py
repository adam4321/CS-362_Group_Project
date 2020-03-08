#!/usr/bin/env python

from tkinter import font
from tkinter import *

class Window(Frame):

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.master = master

        # self.pack(fill=BOTH, expand=1)
        self.grid(sticky=N+S+E+W)

        # input validation
        vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        # number read out field
        self.displayField = Entry(self, validate='key', validatecommand=vcmd, justify=RIGHT)
        self.displayField.insert(END, '0')
        self.displayField.grid(row=0, column=0, rowspan=2, columnspan=25, ipadx=2, ipady=2, padx=5, pady=5, sticky=N+S+E+W)

        # number and function buttons
        calcButtons = ["sin", "cos", "|x|", "x!", "1/x", "7", "8", "9", "√x", "x^2",
                       "4", "5", "6", "-", "/", "1", "2", "3", "+", "*", "+/-", "0", ".", "C"]
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
    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
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


    # returns current value of entry field
    def doCallBack(self, method):
        number = float(self.displayField.get())
        print(f'came from button: {method}')
        print(f'displayField: {number}')


root = Tk()                             # declare tikinter UI
root.title("Simple Calculator")         # set display title
# root.geometry("500x500")              # optional fixed size
default_font = font.nametofont("TkDefaultFont")     # create font specification object (for sizing)
default_font.configure(size=24)                     # congifure font ob
root.option_add("*Font", default_font)              # set font ob to be used by our tkinter UI

app = Window(root)                      # create window object

root.mainloop()                         # run main
