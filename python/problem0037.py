#!/usr/bin/env python3
"""Project Euler - Problem 37 Module"""

import pelib

LIMIT = 1000000
FPC = pelib.FastPrimeChecker(LIMIT)


def isTruncatablePrime(number):
    result = False
    str_number = str(number)
    # we already know that number is prime
    for i in range(1, len(str_number)):
        result = True
        l_trunc = int(str_number[i:])
        r_trunc = int(str_number[:i])
        if not (FPC.is_prime(l_trunc) and FPC.is_prime(r_trunc)):
            return False

    return result


def problem37():
    """Problem 37 - Truncatable primes"""

    result = 0
    nrTruncPrimes = 0

    for p in pelib.primes_sieve(LIMIT):
        if isTruncatablePrime(p):
            nrTruncPrimes += 1
            result += p

    return result


def run():
    """Default Run Method"""
    return problem37()

if __name__ == '__main__':
    print("Result: ", run())
