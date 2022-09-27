#!/usr/bin/python3
def print_reverse_list_integer(my_list=[]):
    if my_list:
        for elem in my_list[::-1]:
            print("{:d}".format(elem))
