#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    updated_dict = a_dictionary.copy()
    for key, val in a_dictionary.items():
        if val == value:
            del updated_dict[key]

    return updated_dict
