#!/usr/bin/env python3
"""Project Euler - Problem 49 Module"""

import itertools
import pelib

IGNORE_SEQ_START = 1487

def problem49(nr_of_digits, dist):
    """Problem 49 - Prime permutations"""
    limit = 10 ** nr_of_digits

    fpc = pelib.FastPrimeChecker()

    # Lazy
    result = 0
    skip_set = set()
    for p in pelib.primes_sieve(limit):
        if p < 10 ** (nr_of_digits - 1) or p in skip_set:
            continue

        s = set([p])
        for pp_arr in itertools.permutations(str(p)):
            pp = int("".join(pp_arr))
            if len(str(pp)) == nr_of_digits and fpc.is_prime(pp):
                s.add(pp)

        skip_set.update(s)

        if len(s) > 2:
            # check
            for pe in s:
                if s.issuperset([pe, pe + dist, pe + (2 * dist)]) and pe != IGNORE_SEQ_START:
                    return int(str(pe) + str(pe + dist) + str(pe + (2 * dist)))


def run():
    """Default Run Method"""
    return problem49(4, 3330)

if __name__ == '__main__':
    print("Result: ", run())
