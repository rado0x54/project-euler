#!/usr/bin/env python3
"""Project Euler - Problem 71 Module"""

from fractions import Fraction

# Smallest Distance if 7 & new_d have no common devisors
# 3/7 -> 3*5 / 7*5 -> 15 / 35 -> (closest) 14 / 35 = 2/5
# 3/7 -> 3*7 / 7*7 -> bad
# 3/7 -> 3*3 / 7*3 -> 9 / 21 -> (closest) 7 / 21 = 1/3


# direction = {-1,1} == {left, right} (neighbor)
def closest_neighbor_fraction(des_denominator, divider_fraction, direction):
    # print("des_denominator={} divider_fraction={} direction={}".format(des_denominator, divider_fraction, direction))
    if des_denominator % divider_fraction.denominator == 0:
        return (divider_fraction.numerator * des_denominator // divider_fraction.denominator) + direction

    greatest_numerator = divider_fraction.numerator * des_denominator
    # print("range end {}".format(direction*divider_fraction.denominator))
    for diff in range(direction, direction*divider_fraction.denominator, direction):
        # print("greatest_numerator={} diff={}".format(greatest_numerator, diff))
        if (greatest_numerator + diff) % divider_fraction.denominator == 0:
            # print("test")
            return (greatest_numerator + diff) // divider_fraction.denominator
            #return Fraction(greatest_numerator + diff, divider_fraction.denominator * des_denominator)


def problem71(max_d, divider_fraction):
    """Problem 71 - Ordered fractions"""

    max_fraction = Fraction()
    for d in range(2, max_d + 1):
        # actually gcd(d,divider_fraction.denominator) should be 1
        # but be know divider_fraction.denominator is prime, so it just must
        # not be a factor.
        if d % divider_fraction.denominator == 0:
            continue

        left_neighbor = Fraction(closest_neighbor_fraction(d, divider_fraction, -1), d)
        # print("left_neighbor={}".format(left_neighbor))
        if left_neighbor > max_fraction:
            max_fraction = left_neighbor

    return max_fraction.numerator


def run():
    """Default Run Method"""
    #return problem71(8, Fraction(3, 7))
    return problem71(1000000, Fraction(3, 7))

if __name__ == '__main__':
    print("Result: ", run())
