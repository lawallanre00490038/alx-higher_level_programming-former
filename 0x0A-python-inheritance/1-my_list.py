#!/usr/bin/python3
"""
this modules contains MyList class
"""


class MyList(list):
    """this si the instances"""
    def __init__(self):
        """this is a subclass"""
        super().__init__()

    def print_sorted(self):
        """printed sorted"""
        print(sorted(self))
