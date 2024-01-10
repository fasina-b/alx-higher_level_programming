#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for new in matrix:
        for add in new:
            print("{:d}".format(add), end=" " if add != new[-1] else "")
        print()
