#!/usr/bin/python3
"""
file
"""


def minOperations(n):
    """
    This function calculates the minimum number of operations 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    x = minOperations(n // 2) + n // 2 
    y = minOperations(n - (n // 2)) + 1
    return min(x, y)
