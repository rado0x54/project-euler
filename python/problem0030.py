#!/usr/bin/env python3
"""Project Euler - Problem 30 Module"""


def problem30(nr_powers):
    """Problem 30 - Digit fifth powers"""
    # upper limit
    p = 1
    while (9 ** nr_powers) * p > (10 ** p):
        p += 1

    upper = 10 ** p
    #print("Upper Limit:",upper)

    def digit_power(input):
        cum = 0
        for d in str(input):
            cum += int(d) ** nr_powers
        return cum

    result = 0
    for x in range(10, upper):
        if x == digit_power(x):
            result += x
            # print(x);

    return result


def run():
    """Default Run Method"""
    return problem30(5)

if __name__ == '__main__':
    print("Result: ", run())
