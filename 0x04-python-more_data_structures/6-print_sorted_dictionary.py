#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    r = sorted(a_dictionary)
    for i in r:
         print("{}: {}".format(i, a_dictionary[i]))
