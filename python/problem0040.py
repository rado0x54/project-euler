#!/usr/bin/env python3
"""Project Euler - Problem 40 Module"""


def problem41(limit):
    """Problem 41 - Champernowne's constant"""
    i = 0
    str_number = ''
    while len(str_number) <= limit:
        str_number += str(i)
        i += 1

    d = 1
    result = 1
    while d <= limit:
        result *= int(str_number[d])
        d *= 10

    return result


def run():
    """Default Run Method"""
    return problem41(1000000)

if __name__ == '__main__':
    print("Result: ", run())
