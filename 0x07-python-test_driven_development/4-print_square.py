#!/usr/bin/python3
"""
this is a code to get the square fron an argument
    
this is a function.print_sqare(size)
"""
def print_square(size):
    """inside the function"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
