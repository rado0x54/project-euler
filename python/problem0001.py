#!/usr/bin/env python3
"""Project Euler - Problem 1 Module"""

def problem1(limit, mod1, mod2):
    """Problem 1"""
    result = 0

    for cur in range(0, limit):
        if cur % mod1 == 0 or cur % mod2 == 0:
            result += cur

    return result

def run():
    """Default Run Method"""
    return problem1(1000, 3, 5)

if __name__ == '__main__':
    print("Result: ", run())
