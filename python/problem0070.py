#!/usr/bin/env python3
"""Project Euler - Problem 70 Module"""

from fractions import Fraction

from problem0069 import eulers_totient


def problem70(limit):
    """Problem 70 - Totient permutation"""
    # use example as upper bound.
    min_totient_quotient = Fraction(87109, 79180)
    min_i = 0
    for i, phi in eulers_totient(limit):
        str_i = str(i)
        str_phi = str(phi)
        if len(str_i) == len(str_phi) and sorted(str_i) == sorted(str_phi):
            q = Fraction(i, phi)
            # print("i:{} phi:{} q:{},min_q:{}, min_i:{}".format(i,phi,q,min_totient_quotient,min_i))
            if q < min_totient_quotient:
                min_totient_quotient = q
                min_i = i

    return min_i


def run():
    """Default Run Method"""
    return problem70(10000000)

if __name__ == '__main__':
    print("Result: ", run())
