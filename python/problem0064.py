#!/usr/bin/env python3
"""Project Euler - Problem 64 Module"""

import math

def square_root_contined_fraction(n):
    """Generator for getting the a_n of the root fractions"""
    # int(!), current_nominator = sqrt(n) - current_subtraction
    current_subtraction = 0
    current_denominator = 1  # int(!), initial case sq_n / 1
    floor_sq_n = math.floor(math.sqrt(n))
    #print("floor_sq_n:{}".format(floor_sq_n))

    sub_den_set = set()

    # the loop expects (sqrt(n) - current_addition)/current_denominator > 1
    while True:
        # print("current_subtraction:{} current_denominator:{}".format(
        #     current_subtraction, current_denominator))

        a_n = 0  # currentcount.
        # One substraction is always possible due to condition that faction > 1
        while (current_subtraction + current_denominator) <= floor_sq_n:
            current_subtraction += current_denominator
            a_n += 1
        yield a_n

        # calculate new values:
        #print("current_subtraction:{}".format(current_subtraction))
        current_denominator = (n - (current_subtraction ** 2)) // current_denominator
        current_subtraction = -current_subtraction

        # Perfect roots OR Cancel generator on repeat
        key = (current_subtraction, current_denominator)
        if current_denominator == 0 or key in sub_den_set:
            return
        else:
            sub_den_set.add(key)



def square_root_contined_fraction_period_len(n):
    """Returns period length of the root fractions of n"""
    return len(list(square_root_contined_fraction(n)))-1

def problem64(limit):
    """Problem 64 - Odd period square roots"""

    result = 0
    for i in range(1,limit+1):
        period_len = square_root_contined_fraction_period_len(i)
        if period_len % 2 == 1:
            result += 1

    return result


def run():
    """Default Run Method"""
    return problem64(10000)

if __name__ == '__main__':
    print("Result: ", run())
