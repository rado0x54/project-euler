#!/usr/bin/env python3
"""Project Euler - Problem 43 Module"""

import pelib
import itertools

PANDIGITAL = '0123456789'


def check_property(n_str):
    p_gen = pelib.primes_sieve(20)

    property_holds = True
    for i in range(1, len(n_str) - 3 + 1):
        p = next(p_gen)
        n = int(n_str[i:i + 3])
        if n % p != 0:
            property_holds = False
            break

    return property_holds


def problem43():
    """Problem 43 - Sub-string divisibility"""
    result = 0
    for p in itertools.permutations(PANDIGITAL):
        n_str = "".join(p)
        if check_property(n_str):
            result += int(n_str)

    return result


def run():
    """Default Run Method"""
    return problem43()

if __name__ == '__main__':
    print("Result: ", run())
