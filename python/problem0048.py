#!/usr/bin/env python3
"""Project Euler - Problem 48 Module"""


def problem48(limit):
    """Problem 48 - Self powers"""

    # Lazy
    result = 0
    for x in range(1, limit + 1):
        result += x ** x

    return int(str(result)[-10:])


def run():
    """Default Run Method"""
    return problem48(1000)

if __name__ == '__main__':
    print("Result: ", run())
