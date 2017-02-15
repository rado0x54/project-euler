#!/usr/bin/env python3
"""Project Euler - Problem 60 Module"""


import math
from sympy import sieve
from sympy.ntheory import primetest


PRIME_LIMIT = 30000

# Takes current prime array "current" and looks for another prime to extend it


def find_prime_concatenates(current_primes, targetsize, sumlimit, solutions):
    # print("find_prime_concatenates({}, {}, {}, {})".format(
    #     current_primes, targetsize, sumlimit, solutions))
    if len(current_primes) == targetsize:
        solutions.append(current_primes)
        print("Found Solution: {}".format(current_primes))
        return True
    else:
        # 2 can never concat new prime
        left_range = 3
        if len(current_primes) > 0:
            left_range = current_primes[-1] + 1
        for p in sieve.primerange(left_range, sieve._list[-1]):
            # 5 can never concat new prime
            if p == 5:
                continue
            if p > sumlimit:
                break
            if check_new_prime(current_primes, p):
                new_current_primes = list(current_primes)
                new_current_primes.append(p)
                if find_prime_concatenates(new_current_primes, targetsize, sumlimit - p, solutions):
                    return True  # Not, this is a non-perfect optimization because it assumes there is only one solution for a given depth part

    return False


def check_new_prime(current_primes, new_prime):
    for p in current_primes:
        if not is_concat_prime(new_prime, p):
            return False
        if not is_concat_prime(p, new_prime):
            return False

    return True



# Buffer
prime_buffer = {}

# Note Prime Checks can get as high as (PRIME_LIMIT/2)**2
def is_concat_prime(x, y):
    res = concat_int(x, y)
    if res not in prime_buffer:
        prime_buffer[res] = primetest.isprime(res)
    return prime_buffer[res]


def concat_int(x, y):
    a = math.floor(math.log10(y))
    return int(x * 10**(1 + a) + y)


def problem60():
    """Problem 60 - Prime pair sets"""
    sieve.extend(PRIME_LIMIT) # find_prime_concatenates requires non-empty sieve
    solutions = []
    find_prime_concatenates([], 5, PRIME_LIMIT, solutions)
    return min(sum(s) for s in solutions)


def run():
    """Default Run Method"""
    return problem60()

if __name__ == '__main__':
    print("Result: ", run())
