#!/usr/bin/env python3
"""Project Euler - Problem 33 Module"""

from fractions import Fraction


def problem33(nr_digits):
    """Problem 33 - Digit canceling fractions"""

    a_sum = 1
    b_sum = 1
    for a in range(10**(nr_digits - 1), (10**nr_digits) - 1):
        for b in range(a + 1, 10**nr_digits):
            # print(a/b);

            a_str = str(a)
            b_str = str(b)

            for sa in range(0, nr_digits):
                if a_str[sa] == '0':
                    continue

                # check in b
                for sb in range(0, nr_digits):
                    if (a_str[sa] == b_str[sb]):
                        a_short = a_str[:sa] + a_str[sa + 1:]
                        b_short = b_str[:sb] + b_str[sb + 1:]
                        a_short_int = int(a_short)
                        b_short_int = int(b_short)
                        if (b_short_int == 0):
                            continue

                        if (a / b == a_short_int / b_short_int):
                            a_sum *= a_short_int
                            b_sum *= b_short_int
                            #print(a_str, "/", b_str, "->",
                            #      a_short, "/", b_short)

    return Fraction(a_sum, b_sum).denominator


def run():
    """Default Run Method"""
    return problem33(2)

if __name__ == '__main__':
    print("Result: ", run())
