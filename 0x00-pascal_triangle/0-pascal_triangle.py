#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    triangle = []

    if not isinstance(n, int) or n <= 0:
        return triangle

    list = 0
    while list < n:
        line = []
        j = 0
        while j < list + 1:
            if j == 0 or j == list:
                line.append(1)
            elif list > 0 and j > 0:
                line.append(triangle[list - 1][j - 1] + triangle[list - 1][j])
            j += 1
        triangle.append(line)
        list += 1

    return triangle
