#!/usr/bin/env python3
"""Project Euler - Problem 35 Module"""

import pelib

def is_circular_primes(number, fpc):
    str_number = str(number)
    # we already know that number is prime
    for i in range(1, len(str_number)):
        # shift
        shifted = int(str_number[i:] + str_number[:i])
        if not fpc.is_prime(shifted):
            return False

    return True

def problem35(limit):
    """Problem 35 - Circular primes"""
    fpc = pelib.FastPrimeChecker(limit)
    
    result = 0
    for p in pelib.primes_sieve(limit):
        if is_circular_primes(p, fpc):
            result += 1

    return result


def run():
    """Default Run Method"""
    return problem35(1000000)

if __name__ == '__main__':
    print("Result: ", run())
