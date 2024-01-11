#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = dict(a_dictionary)
    for r, v in my_dict.items():
        my_dict[r] = v * 2
        return my_dict
