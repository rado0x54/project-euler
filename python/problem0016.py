#!/usr/bin/env python3
"""Project Euler - Problem 16 Module"""

def problem16(exponent):
    """Problem 16 - Power digit sum"""
    number = 2 ** exponent

    result = 0
    for x in str(number):
        result += int(x)

    return result


def run():
    """Default Run Method"""
    return problem16(1000)

if __name__ == '__main__':
    print("Result: ", run())
