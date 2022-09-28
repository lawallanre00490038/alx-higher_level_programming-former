#!/usr/bin/python3
def print_sorted_dictionary(dic):
    for key in sorted(dic.keys()):
        print("{:s}: {}".format(key, dic[key]))
