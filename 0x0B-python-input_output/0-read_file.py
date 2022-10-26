#!/usr/bin/python3
"""
This module contains the function that reads a file
"""
def read_file(filename=""):
    """this function reads a file as the arguments given"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
