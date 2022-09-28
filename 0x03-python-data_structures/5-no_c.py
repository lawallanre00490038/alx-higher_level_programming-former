#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for elem in my_string:
        if elem != "c" and elem != "C":
            new_string += elem
    return new_string
