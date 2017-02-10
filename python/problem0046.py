#!/usr/bin/env python3
"""Project Euler - Problem 46 Module"""

import math
import pelib


def check_goldbach(n):
    if pelib.is_prime(n):
        return True

    for p in pelib.primes_sieve(n):
        np2 = (n - p) / 2
        np2_root = math.sqrt(np2)
        if np2_root == int(np2_root):
            return True

    return False


def problem46(limit):
    """Problem 46 - Goldbach's other conjecture"""

    for x in range(3, limit, 2):
        if not check_goldbach(x):
            return x


def run():
    """Default Run Method"""
    return problem46(10000000)

if __name__ == '__main__':
    print("Result: ", run())
