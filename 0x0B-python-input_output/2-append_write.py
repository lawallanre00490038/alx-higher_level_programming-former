#!/usr/bin/python3
"""
this is a module that the function appends a file to another file
"""
def append_write(filename="", text=""):
    """this function appends text to a function"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
