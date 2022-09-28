#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def sr_elem(elem):
        return (elem if elem != search else replace)
    return list(map(sr_elem, my_list))
