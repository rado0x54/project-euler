#!/usr/bin/env python3
"""Project Euler - Problem 73 Module"""

from fractions import Fraction
from problem0071 import closest_neighbor_fraction

# Smallest Distance if 7 & new_d have no common devisors
# 2: 1/2
# 3: 1/3 & 2/3
# 4: 1/4 (2/4) 3/4
# 5: 1/5 2/5 3/5 4/5
# 6: 1/6 (2/6) (3/6) (4/6) 5/6
# -> Nr of values for d == phi(d)

# Only Count Fractions ]1/3,1/2[

def problem73(limit_d, lower_limit, upper_limit):
    """Problem 73 - Counting fractions in a range"""

    result = 0
    for d in range(2, limit_d+1):
        right_lower = closest_neighbor_fraction(d, lower_limit, 1)
        left_upper = closest_neighbor_fraction(d, upper_limit, -1)

        for i in range(right_lower, left_upper+1):
            # Only add Fractions that have not been added before
            if Fraction(i, d).denominator == d: # This is clearly not efficient :)
                result += 1
    return result

def run():
    """Default Run Method"""
    return problem73(12000, Fraction(1, 3), Fraction(1, 2))

if __name__ == '__main__':
    print("Result: ", run())
