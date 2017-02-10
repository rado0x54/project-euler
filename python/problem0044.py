#!/usr/bin/env python3
"""Project Euler - Problem 44 Module"""

import math

def isPentagonal(x):
    p = 1 + math.sqrt(1 + (24 * x))
    return p == int(p) and p % 6 == 0


def problem44(limit, mod1, mod2):
    """Problem 44 - Pentagon numbers"""
    i = 1
    step = 4
    sequence = []

    d = -1
    while d < step:
        # Look for smallest neighbor that meets criteria
        for pn in sequence:
            pn_add = i + pn
            pn_diff = i - pn
            if isPentagonal(pn_add) and isPentagonal(pn_diff) and (d < 0 or pn_diff < d):
                d = pn_diff
                # print(i, pn, d)

        sequence.append(i)
        i += step
        step += 3

    return d


def run():
    """Default Run Method"""
    return problem44(1000, 3, 5)

if __name__ == '__main__':
    print("Result: ", run())
