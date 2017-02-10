#!/usr/bin/env python3
"""Project Euler - Problem 27 Module"""

def problem27(ab_limit):
    """Problem 27 - Quadratic primes"""
    # upper limit
    nr_primes = 2 * ab_limit * ab_limit + ab_limit
    primes = [1] * (nr_primes - 2)
    result = 0

    for x in range(2, nr_primes):
        if primes[x - 2] == 1:
            # x is Prime, eliminate x*y for y > 1
            y = (x - 2) + x
            while y < nr_primes - 2:
                primes[y] = 0
                y += x

    # Largest seq
    l_seq = 0
    for a in range(-ab_limit + 1, ab_limit):
        for b in range(2, ab_limit):
            if primes[b - 2] == 0:
                continue  # no prime
            # check formula
            seq = 1
            x = 2
            while True:
                v = (x**2) + (a * x) + b
                if v > 1 and primes[v - 2] == 1:
                    seq += 1
                else:
                    break

                x += 1

            if seq > l_seq:
                l_seq = seq
                result = a * b

    return result

def run():
    """Default Run Method"""
    return problem27(1000)

if __name__ == '__main__':
    print("Result: ", run())
