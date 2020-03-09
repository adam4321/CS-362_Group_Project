"""
Final Project CS-362
Oregon State University Winter term 2020
Group 7

File that defines the supported math operations
"""

import math

def multiplication(op1, op2):
    val = op1 * op2
    return round(val, 6)

def division(op1, op2):
    if op2 == 0:
        return "Invalid Input, cannot divide by 0"
    else:
        val = op1 / op2
        return round(val, 6)

def square_root(op1):
    if op1 < 0:
        return "Invalid Input"
    else:
        val = math.sqrt(op1)
        return round(val, 6)

def power_two(op1):
    val = op1 * op1
    return val

def inverse(op1):
    val = 1 / op1
    return round(val, 6)

def factorial(op1):
    if op1 % 1 != 0:
        return "Must be an integer"
    if op1 < 0:
        return "Invalid Input"
    if op1 == 1 or op1 == 0:
        return 1
    else:
        return op1 * factorial(op1 - 1)

def absolute_val(op1):
    return abs(op1)

def sine(op1):
    val = round(math.sin(op1), 6)
    return val

def cosine(op1):
    val = round(math.cos(op1), 6)
    return val
