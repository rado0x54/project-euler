#!/usr/bin/env python3
"""Project Euler - Problem 34 Module"""

import math


def problem34():
    """Problem 34 - Digit factorials"""

    n = 1
    while True:
        if math.factorial(9) * n < 10 ** n:
            break
        n += 1

    limit = 10 ** (n - 2)

    result = 0
    for x in range(10, limit):
        sum = 0
        for y in str(x):
            sum += math.factorial(int(y))
            if sum > x:
                break

        if sum == x:
            result += x

    return result


def run():
    """Default Run Method"""
    return problem34()

if __name__ == '__main__':
    print("Result: ", run())
