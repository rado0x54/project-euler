#!/usr/bin/env python3
"""Project Euler - Problem 72 Module"""

from problem0069 import eulers_totient

# Smallest Distance if 7 & new_d have no common devisors
# 2: 1/2
# 3: 1/3 & 2/3
# 4: 1/4 (2/4) 3/4
# 5: 1/5 2/5 3/5 4/5
# 6: 1/6 (2/6) (3/6) (4/6) 5/6
# -> Nr of values for d == phi(d)

def problem72(limit):
    """Problem 72 - Counting fractions"""

    result = 0
    for i, phi in eulers_totient(limit+1):
        result += phi

    return result

def run():
    """Default Run Method"""
    return problem72(1000000)

if __name__ == '__main__':
    print("Result: ", run())
