#!/usr/bin/python3
"""
this function prints values that are excluding 
",", ".", ";" but can prits spaces
"""
def text_indentation(text):
    """this is  a function that prints a value that are excluding ; , . """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for t in text:
        if flag == 0:
            if t == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if t in ("?", ".", ":"):
                print(t)
                print()
                flag = 0
            else:
                print(t, end="")
