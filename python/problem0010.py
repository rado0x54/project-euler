#!/usr/bin/env python3
"""Project Euler - Problem 10 Module"""

def problem10(limit):
    """Problem 10 - Summation of primes"""
    primes = [1] * (limit-2)

    for x in range(2, limit):
        if primes[x-2] == 1:
            # x is Prime, eliminate x*y for y > 1
            y = (x-2) + x
            while y < limit-2:
                primes[y] = 0
                y += x

    result = 0
    current = 2
    for x in primes:
        if x == 1:
            result += current
        current += 1

    return result

def run():
    """Default Run Method"""
    return problem10(2000000)

if __name__ == '__main__':
    print("Result: ", run())
