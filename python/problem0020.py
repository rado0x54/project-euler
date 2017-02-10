#!/usr/bin/env python3
"""Project Euler - Problem 20 Module"""

import math

def problem20(number):
    """Problem 20 - Factorial digit sum"""
    fact_number = math.factorial(number)

    result = 0
    for x in str(fact_number):
        result += int(x)

    return result






def run():
    """Default Run Method"""
    return problem20(100)

if __name__ == '__main__':
    print("Result: ", run())
