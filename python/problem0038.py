#!/usr/bin/env python3
"""Project Euler - Problem 38 Module"""


def check_pandigital_multiple(n, pandigital_size):
    i = 1
    number = ''
    while len(number) < pandigital_size:
        number += str(n * i)
        i += 1

    if len(number) == pandigital_size and ''.join(sorted(number)) == '123456789':
        return int(number)

    return 0


def problem38(pandigital_size):
    """Problem 38 - Pandigital multiples"""

    # Limit:
    limit = int((10**(int((pandigital_size + 1) / 2))) / 2)

    result = 0
    for i in range(1, limit):
        pandigital = check_pandigital_multiple(i, pandigital_size)
        if pandigital > 0 and pandigital > result:
            # print(i,pandigital)
            result = pandigital

    return result


def run():
    """Default Run Method"""
    return problem38(9)

if __name__ == '__main__':
    print("Result: ", run())
