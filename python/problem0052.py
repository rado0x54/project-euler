#!/usr/bin/env python3
"""Project Euler - Problem 52 Module"""

import pelib


def problem52():
    """Problem 52 - Permuted multiples"""

    x = 1
    while True:
        ss_str_2x = sorted(set(str(2 * x)))
        ss_str_3x = sorted(set(str(3 * x)))
        ss_str_4x = sorted(set(str(4 * x)))
        ss_str_5x = sorted(set(str(5 * x)))
        ss_str_6x = sorted(set(str(6 * x)))
        if ss_str_2x == ss_str_3x == ss_str_4x == ss_str_5x == ss_str_6x:
            #print(x, ss_str_2x)
            return x

        x += 1


def run():
    """Default Run Method"""
    return problem52()

if __name__ == '__main__':
    print("Result: ", run())
