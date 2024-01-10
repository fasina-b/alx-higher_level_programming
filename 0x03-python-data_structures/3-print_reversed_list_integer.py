#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
<<<<<<< HEAD
        for a in range(len(my_list)):
            print("{:d}".format(my_list[a]))
=======
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
>>>>>>> fd733d5b888b5bc144da826b8f8f73193bab66f2
