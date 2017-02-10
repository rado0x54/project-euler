#!/usr/bin/env python3
"""Project Euler - Problem 1 Module"""

def problem7(nr_of_prime):
    """Problem 7 - 10001st prime"""
    primelist = []

    i = 2
    while len(primelist) < nr_of_prime:
        prime = True
        for x in primelist:
            if i % x == 0:
                prime = False
                break
        if prime:
            primelist.append(i)
        i = i+1

    return primelist[-1]


def run():
    """Default Run Method"""
    return problem7(10001)

if __name__ == '__main__':
    print("Result: ", run())
