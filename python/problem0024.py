#!/usr/bin/env python3
"""Project Euler - Problem 24 Module"""

import itertools

def problem24(nr_permutation):
    """Problem 24 - Lexicographic permutations"""
    return int(''.join(list(itertools.permutations(DIGITS))[nr_permutation-1]))

DIGITS = '0123456789'

def run():
    """Default Run Method"""
    return problem24(1000000)

if __name__ == '__main__':
    print("Result: ", run())
