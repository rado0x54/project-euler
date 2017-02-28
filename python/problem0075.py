#!/usr/bin/env python3
"""Project Euler - Problem 75 Module"""

from pelib import fibonacci_generator
from collections import deque

from math import gcd
from itertools import count


def problem75(input_max_length):
    """Problem 75 - Singular integer right triangles"""

    max_length = input_max_length+1
    # for m > n > 0
    # a=m^{2}-n^{2},\ \,b=2mn,\ \,c=
    # a + b + c = m^{2} - n^{2} + 2mn + m^{2} + n^{2} = 2m^2+2mn
    # if n == 1: l = 2m^2+2m -> m1/2 = -2 + sqrt(4 - 4*2*l)/2

    len_count = [0] * max_length

    for m in count(2, 1):
        for n in range(1, m):

            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2

            l = a + b + c

            if gcd(m, n) == 1 and (m%2 == 0 or n%2 == 0) and l < max_length:
                for l_step in range(l, max_length, l):
                    len_count[l_step] += 1

            # Break condition l is > max_length for smallest n
            if l > max_length and n == 1:
                return len_count.count(1)


def run():
    """Default Run Method"""
    return problem75(1500000)

if __name__ == '__main__':
    print("Result: ", run())
