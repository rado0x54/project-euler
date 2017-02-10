#!/usr/bin/env python3
"""Project Euler - Problem 41 Module"""

import itertools
import pelib

PANDIGITAL = '123456789'

def problem41():
    """Problem 41 - Pandigital prime"""
    for i in range(len(PANDIGITAL), 1, -1):
        cur_max = 0
        for p in itertools.permutations(PANDIGITAL[:i]):
            n = int("".join(p))
            if pelib.is_prime(n) and n > cur_max:
                cur_max = n

        if cur_max > 0:
            return cur_max


def run():
    """Default Run Method"""
    return problem41()

if __name__ == '__main__':
    print("Result: ", run())
