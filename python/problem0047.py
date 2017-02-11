#!/usr/bin/env python3
"""Project Euler - Problem 47 Module"""

import pelib


def problem47(nr_distinct_prime_factors, nr_consecutive):
    """Problem 47 - Distinct primes factors"""

    x = 2
    consecutive = 0
    while True:

        unique = set(pelib.get_prime_factors(x))
        if len(unique) == nr_distinct_prime_factors:
            consecutive += 1
        else:
            consecutive = 0

        if consecutive == nr_consecutive:
            return x - nr_consecutive + 1

        x += 1


def run():
    """Default Run Method"""
    return problem47(4, 4)

if __name__ == '__main__':
    print("Result: ", run())
