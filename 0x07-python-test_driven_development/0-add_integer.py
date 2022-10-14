#!/usr/bin/python3
"""
this modules has a function names `add_integer` that 
adds integers `a` and `b`

""" 
def add_integer(a, b=98):
    """this function returns an adittion of a and b"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a =int(a)
    if type(b) is float:
        b = int(b)
    return(a + b)
