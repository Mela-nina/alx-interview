#!/usr/bin/python3
"""
The Minimum operations
"""


def minOperations(n):
    """
    This returns the fewest number of operation need
    to result in exactly n H characters in the file
    """
    s = 0
    t = 2
    while n > 1:
        while n % t == 0:
            s += t
            n = n / t
        t += 1
    return s
