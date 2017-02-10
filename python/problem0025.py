#!/usr/bin/env python3
"""Project Euler - Problem 1 Module"""

def problem25(nr_of_digits):
    """Problem 25 - 1000-digit Fibonacci number"""
    n_1 = 1
    n_2 = 1

    seq = 3
    while True:
        n = n_1 + n_2
        if (n / 10 ** (nr_of_digits-1)) >= 1:
            break

        n_2 = n_1
        n_1 = n

        seq += 1

    return seq

def run():
    """Default Run Method"""
    return problem25(1000)

if __name__ == '__main__':
    print("Result: ", run())
