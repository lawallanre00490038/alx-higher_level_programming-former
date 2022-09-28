#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for elem in my_string:
        if elem == "c" or elem == "C":
            continue
        new_string += elem
