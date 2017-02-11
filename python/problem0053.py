#!/usr/bin/env python3
"""Project Euler - Problem 53 Module"""

import pelib


def problem53(n_limit, lower_limit):
    """Problem 53 - Combinatoric selections"""

    # must be > 23
    n = 23

    result = 0
    while n <= n_limit:
        for k in range(2, n_limit):
            if pelib.choose(n, k) > lower_limit:
                result += 1

        n += 1

    return result


def run():
    """Default Run Method"""
    return problem53(100, 1000000)

if __name__ == '__main__':
    print("Result: ", run())
