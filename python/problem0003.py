#!/usr/bin/env python3
"""Project Euler - Problem 1 Module"""

def problem3(number):
    """Prime Factorization"""

    i = 2
    while i * i < number:
        while number % i == 0:
            number /= i
        i += 1

    return int(number)


def run():
    """Default Run Method"""
    return problem3(600851475143)

if __name__ == '__main__':
    print("Result: ", run())
