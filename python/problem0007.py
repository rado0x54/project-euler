#!/usr/bin/env python3
"""Project Euler - Problem 1 Module"""

from sympy import sieve

def problem7(nr_of_prime):
    """Problem 7 - 10001st prime"""

    # old code :)
    # primelist = []

    # i = 2
    # while len(primelist) < nr_of_prime:
    #     prime = True
    #     for x in primelist:
    #         if i % x == 0:
    #             prime = False
    #             break
    #     if prime:
    #         primelist.append(i)
    #     i = i+1

    sieve.extend_to_no(nr_of_prime)
    return sieve._list[nr_of_prime-1]


def run():
    """Default Run Method"""
    return problem7(10001)

if __name__ == '__main__':
    print("Result: ", run())
