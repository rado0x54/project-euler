#!/usr/bin/env python3
"""Project Euler - Problem 22 Module"""

import string
import os

def problem22(filename):
    """Problem 22 - Names scores"""
    names = []

    # read file
    with open(filename, 'r') as f:
        for line in f:
            names = [x.strip('"') for x in line.split(',')]

    name_counter = 1
    result = 0

    for name in sorted(names):
        cum = 0
        for letter in name:
            cum += string.ascii_uppercase.index(letter) + 1

        result += name_counter * cum
        name_counter += 1

    return result


FILENAME = 'problem0022.txt'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def run():
    """Default Run Method"""
    return problem22(os.path.join(__location__, FILENAME))

if __name__ == '__main__':
    print("Result: ", run())
