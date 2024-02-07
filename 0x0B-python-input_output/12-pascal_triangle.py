#!/usr/bin/python3
"""
Contains a function to generate Pascal's triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """ Generate Pascal's triangle as a list of lists """

    triangle = []
    if n == 0:
        return triangle

    triangle.append([1])

    for _ in range(1, n):
        before = triangle[-1]
        after = [1]
        for i in range(len(before) - 1):
            after.append(before[i] + before[i + 1])
        after += [1]
        triangle.append(after)

    return triangle
