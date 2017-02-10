#!/usr/bin/env python3
"""Project Euler - Problem 12 Module"""

def number_of_devisors(p):
    if p == 1:
        return 1

    nr = 2 # 1 and p.
    x = 2
    while x < p/x:
        if p % x == 0:
            nr += 2 # x and p/x
        x += 1
    return nr


def problem12(nr_divisors):
    """Problem 12 - Highly divisible triangular number"""

    x = 1
    cur = 0
    while True:
        cur += x
        nr = number_of_devisors(cur)
        if nr >= nr_divisors:
            break
        x += 1

    return cur

def run():
    """Default Run Method"""
    return problem12(500)

if __name__ == '__main__':
    print("Result: ", run())
