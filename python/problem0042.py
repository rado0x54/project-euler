#!/usr/bin/env python3
"""Project Euler - Problem 42 Module"""

import math
import os
import string


def is_triangle_number(x):
    n = math.sqrt(1 + (8 * x))
    return n == int(n) and n % 2 == 1


def problem42(filename):
    """Problem 42 - Coded triangle numbers"""
    words = []
    # read file
    with open(filename, 'r') as f:
        for line in f:
            words = [x.strip('"') for x in line.split(',')]

    result = 0
    for word in words:
        sum = 0
        for x in word:
            sum += string.ascii_uppercase.index(x) + 1

        if is_triangle_number(sum):
            result += 1

    return result

FILENAME = 'problem0042.txt'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run():
    """Default Run Method"""
    return problem42(os.path.join(__location__, FILENAME))

if __name__ == '__main__':
    print("Result: ", run())
