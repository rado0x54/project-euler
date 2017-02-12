#!/usr/bin/env python3
"""Project Euler - Problem 56 Module"""


def problem56(a_limit, b_limit):
    """Problem 56 - Powerful digit sum"""

    max = 0
    for a in range(1, a_limit):
        for b in range(1, b_limit):
            p_ab_sum_digits = sum(int(x) for x in str(a ** b))
            if p_ab_sum_digits > max:
                max = p_ab_sum_digits

    return max


def run():
    """Default Run Method"""
    return problem56(100, 100)

if __name__ == '__main__':
    print("Result: ", run())
