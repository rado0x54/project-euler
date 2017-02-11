#!/usr/bin/env python3
"""Project Euler - Problem 50 Module"""

import pelib


def problem50(limit):
    """Problem 50 - Prime permutations"""

    fpc = pelib.FastPrimeChecker(limit + 1)

    # Lazy
    tsum = 0
    longest = 0
    highest_sum = 0
    primes = []
    for p in pelib.primes_sieve(limit):
        primes.append(p)
        tsum += p
        # print(p,sum)

        if tsum - sum(primes[0:len(primes) - longest]) > limit:
            break

        i = len(primes) - longest

        # Subtract from front
        for i in range(0, len(primes)):
            seqlen = len(primes) - i
            if seqlen <= longest:
                break

            psum = tsum - sum(primes[0:i])
    # 		print(tsum,sum(primes[0:i]),psum,seqlen)

            if fpc.is_prime(psum):
                longest = seqlen
                highest_sum = psum

    return highest_sum


def run():
    """Default Run Method"""
    return problem50(1000000)

if __name__ == '__main__':
    print("Result: ", run())
