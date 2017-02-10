#!/usr/bin/env python3
"""Project Euler - Problem 26 Module"""

import math

def calc_rec_cycle(number):
    """calculate recurring cycle of 1/n"""
    result = 0
    i = 10 ** (int(math.log10(number)) + 1)
    s = set()

    while True:
        if i == number or i == 0:
            result = 0
            break

        if i < number:
            result += 1
            i *= 10
            continue

        # i > n
        r = i % number
        #print('r',r)
        if r not in s:
            result += 1
            s.add(r)
        else:
            break

        i = r * 10
    return result

def problem26(limit):
    """Problem 26 - Reciprocal cycles"""
    result = 0
    result_d = 0

    for d in range(2, limit):
        d_cycle = calc_rec_cycle(d)
        if d_cycle > result:
            result = d_cycle
            result_d = d

    return result_d


def run():
    """Default Run Method"""
    return problem26(1000)

if __name__ == '__main__':
    print("Result: ", run())
