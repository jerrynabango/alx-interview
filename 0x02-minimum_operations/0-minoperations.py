#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """ calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0
    a = 2
    result = 0
    while a <= n:
        if n % a == 0:
            result += a
            n = n / a
        else:
            a += 1
    return result
