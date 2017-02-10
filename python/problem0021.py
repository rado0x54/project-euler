#!/usr/bin/env python3
"""Project Euler - Problem 21 Module"""

import pelib

def problem21(limit):
    """Problem 21 - Amicable numbers"""
    result = 0
    for x in range(2, limit):
        y = pelib.sum_of_devisors(x)
        if y > x and y < limit:
            if pelib.sum_of_devisors(y) == x:
                result += x + y

    return result

def run():
    """Default Run Method"""
    return problem21(10000)

if __name__ == '__main__':
    print("Result: ", run())
