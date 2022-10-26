#!/usr/bin/python3
"""
this is the function that writes a texts into a text file
"""
def write_file(filename="", text=""):
    """this is the fuunction in the module"""
    with open(filename, 'w') as f:
        f.write(text)

    with open(filename, "r", encoding="utf-8") as fl:
        myFile = fl.read()
        count = 0
        for lines in myFile:
            line = lines.split()
            for word in line:
                for char in word:
                    count += 1
    return(count)
