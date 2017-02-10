#!/usr/bin/env python3
"""Project Euler - Problem 32 Module"""

import itertools


def problem32(limit, mod1, mod2):
    """Problem 32 - Pandigital products"""
    s = set()
    result = 0
    for perm in itertools.permutations(VALS):
        for x in range(1, len(VALS)):
            for y in range(x + 1, len(VALS)):
                a = int(''.join(perm[:x]))
                b = int(''.join(perm[x:y]))
                c = int(''.join(perm[y:]))

                if a * b == c and not c in s:
                    s.add(c)
                    result += c

    return result

VALS = '123456789'

def run():
    """Default Run Method"""
    return problem32(1000, 3, 5)

if __name__ == '__main__':
    print("Result: ", run())
