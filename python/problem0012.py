#!/usr/bin/env python3
"""Project Euler - Problem 12 Module"""

from sympy import sieve

MAX_PRIME = 100000


def number_of_devisors(n):
    if n == 1:
        return 1

    # nr_div = 2 # 1 and p.
    # x = 2
    # while x < p/x:
    #     if p % x == 0:
    #         nr_div += 2 # x and p/x
    #     x += 1

    should_print = False
    if n < 10:
        should_print = True

    nr_div = 1
    for p in sieve.primerange(2, n + 1):
        if p * p > n:
            nr_div *= 2
            break

        exponent = 0
        while n % p == 0:
            exponent += 1
            n = n // p

        if exponent > 0:
            nr_div *= exponent + 1

        if n == 1:
            break
            
    return nr_div


def problem12(nr_divisors):
    """Problem 12 - Highly divisible triangular number"""
    sieve.extend(MAX_PRIME)

    x = 1
    while True:
        nr = number_of_devisors(x)
        if x % 2 == 0:  # even
            nr = number_of_devisors(x // 2) * number_of_devisors(x + 1)
        else:  # uneven
            nr = number_of_devisors(x) * number_of_devisors((x + 1) // 2)
        if nr >= nr_divisors:
            break
        x += 1

    return x * (x + 1) // 2


def run():
    """Default Run Method"""
    return problem12(500)

if __name__ == '__main__':
    print("Result: ", run())
