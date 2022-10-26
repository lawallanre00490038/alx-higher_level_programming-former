#!/usr/bin/python3
"""
this is the function that writes a texts into a text file
"""
def write_file(filename="", text=""):
    """this is the fuunction in the module"""
    with open(filename, 'w', encoding="utf-8") as f:
        chars = f.write(text)
    return(chars)
