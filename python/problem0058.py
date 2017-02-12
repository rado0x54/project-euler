#!/usr/bin/env python3
"""Project Euler - Problem 58 Module"""

import pelib


def diagonal_square_spiral():
    """Generate diagonal values of the square spiral"""
    cur_number = 1
    cur_dist = 0
    i = 0
    while True:
        yield cur_number
        # Set Values for next iteration
        if i % 4 == 0:
            cur_dist += 2
        cur_number += cur_dist
        i += 1


def problem58():
    """Problem 58 - Spiral primes"""

    fpc = pelib.FastPrimeChecker()

    result = 0
    nr_primes = 0
    nr_total = 0
    diagonal_square_spiral_gen = diagonal_square_spiral()
    while True:
        value = next(diagonal_square_spiral_gen)

        if fpc.is_prime(value):
            nr_primes += 1
        nr_total += 1

        if nr_total % 4 == 1:
            # print("Side Length: {} Fraction {}/{} = {}".format((nr_total +
            #                                                     1) // 2, nr_primes, nr_total, nr_primes / nr_total))
            # Full Square
            if (nr_primes / nr_total) < .1 and nr_total > 1:  # Exclude "1"-case

                # Side Length
                return (nr_total + 1) // 2

    return result


def run():
    """Default Run Method"""
    return problem58()

if __name__ == '__main__':
    print("Result: ", run())
