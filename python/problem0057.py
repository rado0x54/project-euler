#!/usr/bin/env python3
"""Project Euler - Problem 57 Module"""

from fractions import Fraction


def problem57(limit):
    """Problem 57 - Square root convergents"""

    result = 0
    cur = Fraction()  # == 0
    for _ in range(limit):
        cur = Fraction(1, Fraction(2) + cur)
        val = Fraction(1) + cur
        if len(str(val.numerator)) > len(str(val.denominator)):
            result += 1

    return result


def run():
    """Default Run Method"""
    return problem57(1000)

if __name__ == '__main__':
    print("Result: ", run())
