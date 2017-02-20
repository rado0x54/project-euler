#!/usr/bin/env python3
"""Project Euler - Problem 69 Module"""

from fractions import Fraction

# Generate a list containing all the prime of factors n
def primes_sieve_factors(limit):
    offset = 2  # no 0 & 1 case.
    offset_limit = limit - offset
    if offset_limit > 0:
        # Initialize the primality list
        factor_sieve = [[] for i in range(offset_limit)]

        for (i, factor_list) in enumerate(factor_sieve, start=offset):
            if not factor_list:
                for n in range(i - offset, offset_limit, i):     # Mark factors non-prime
                    factor_sieve[n].append(i)

            yield i, factor_list


def eulers_totient(limit):
    for i, factors in primes_sieve_factors(limit):
        result = Fraction(i)
        # print(i,factors)
        for f in factors:
            result *= Fraction(f - 1, f)
        yield i, result


def problem69(limit):
    """Problem 69 - Totient maximum"""
    max_totient_quotient = Fraction()
    max_i = 0
    for i, phi in eulers_totient(limit + 1):
        q = Fraction(i, phi)
        if q > max_totient_quotient:
            max_totient_quotient = q
            max_i = i

    return max_i


def run():
    """Default Run Method"""
    return problem69(1000000)

if __name__ == '__main__':
    print("Result: ", run())
