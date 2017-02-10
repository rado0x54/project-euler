#!/usr/bin/env python3
"""Project Euler - Problem 39 Module"""


def check_nr_of_solutions(p):
    sum = 0
    for a in range(1, p):
        b = (p * (p - 2 * a)) / (2 * (p - a))
        if (b == int(b) and b > a):
            sum += 1
            # print("p:",p,"Solution:",a,b,p-a-b)

    return sum


def problem39(limit):
    """Problem 39 - Integer right triangles"""
    max_sum = 0
    for p in range(1, limit + 1):
        nr = check_nr_of_solutions(p)
        if (nr > max_sum):
            max_sum = nr
            result = p

    return result


def run():
    """Default Run Method"""
    return problem39(1000)

if __name__ == '__main__':
    print("Result: ", run())
