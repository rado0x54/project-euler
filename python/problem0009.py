#!/usr/bin/env python3
"""Project Euler - Problem 9 Module"""

def problem9(solution):
    """Problem 9 - Special Pythagorean triplet"""

    # Find a^2 + b^2 = c^2 for a < b < c
    a = 1
    while a <= solution/3:
        b = a + 1
        while b <= solution/2:
            c = solution - (a+b)
            if c <= b:
                break
            if (a * a) + (b * b) == (c * c):
                return a * b * c
            b += 1
        a += 1

    # Not Found
    return -1

def run():
    """Default Run Method"""
    return problem9(1000)

if __name__ == '__main__':
    print("Result: ", run())
