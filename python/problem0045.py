#!/usr/bin/env python3
"""Project Euler - Problem 45 Module"""

import math


def isTriangleNumber(x):
    n = math.sqrt(1 + (8 * x))
    return n == int(n) and n % 2 == 1


def isPentagonal(x):
    p = 1 + math.sqrt(1 + (24 * x))
    return p == int(p) and p % 6 == 0


def hexagonal(n):
    return n * ((2 * n) - 1)


def problem45():
    """Problem 45 - Triangular, pentagonal, and hexagonal"""
    hn = 144

    while not (isPentagonal(hexagonal(hn)) and isTriangleNumber(hexagonal(hn))):
        hn += 1

    return hexagonal(hn)


def run():
    """Default Run Method"""
    return problem45()

if __name__ == '__main__':
    print("Result: ", run())
