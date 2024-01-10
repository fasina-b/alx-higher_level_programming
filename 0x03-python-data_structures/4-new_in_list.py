#!/usr/bin/python3
def new_in_list(my_list, idx, element):
<<<<<<< HEAD
    add = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        add[idx] = element
        return add
=======
    new = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        new[idx] = element
        return new
>>>>>>> fd733d5b888b5bc144da826b8f8f73193bab66f2
