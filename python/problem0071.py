#!/usr/bin/env python3
"""Project Euler - Problem 71 Module"""

from fractions import Fraction

# Smallest Distance if 7 & new_d have no common devisors
# 3/7 -> 3*5 / 7*5 -> 15 / 35 -> (closest) 14 / 35 = 2/5
# 3/7 -> 3*7 / 7*7 -> bad
# 3/7 -> 3*3 / 7*3 -> 9 / 21 -> (closest) 7 / 21 = 1/3


def closest_left_fraction(max_d, divider_fraction):

    smallest_distance = divider_fraction
    for d in range(2, max_d + 1):
        # actually gcd(d,divider_fraction.denominator) should be 1
        # but be know divider_fraction.denominator is prime, so it just must
        # not be a factor.
        if d % divider_fraction.denominator:
            continue
        greatest_numerator = divider_fraction.numerator * d
        for diff in range(1, d + 1):
            if (greatest_numerator - diff) % divider_fraction.denominator == 0:
                current_distance = Fraction(
                    diff, divider_fraction.denominator * d)
                if current_distance < smallest_distance:
                    smallest_distance = current_distance
                    break

    return divider_fraction - smallest_distance


def problem71(max_d, divider_fraction):
    """Problem 71 - Ordered fractions"""
    return closest_left_fraction(max_d, divider_fraction).numerator


def run():
    """Default Run Method"""
    # return problem71(8, Fraction(3, 7))
    return problem71(1000000, Fraction(3, 7))

if __name__ == '__main__':
    print("Result: ", run())
