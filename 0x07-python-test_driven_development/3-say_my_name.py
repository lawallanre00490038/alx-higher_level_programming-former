#!/usr/bin/python
"""This is a function that print the cpomombination of 
the arguments as a <firstname> and <lastname>"""
def say_my_name(first_name, last_name=""):
    """This is a inner function doc"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    else:
        print(f"My name is {first_name} {last_name}")
