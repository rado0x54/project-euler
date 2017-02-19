#!/usr/bin/env python3
"""Project Euler - Problem 65 Module"""

from fractions import Fraction
import pelib


def get_nth_convergent_e(n):
    # generate n-1 terms
    faction_terms = [2 * (x + 2) // 3 if (x + 2) %
                     3 == 0 else 1 for x in range(n - 1)]

    lowest_fraction = Fraction()  # == 0
    for i in reversed(faction_terms):
        lowest_fraction = Fraction(1, Fraction(i) + lowest_fraction)

    return Fraction(2, 1) + lowest_fraction

def problem65(n):
    """Problem 65 - Convergents of e"""
    fraction = get_nth_convergent_e(n)
    return pelib.sum_of_digits(fraction.numerator)


def run():
    """Default Run Method"""
    return problem65(100)

if __name__ == '__main__':
    print("Result: ", run())
