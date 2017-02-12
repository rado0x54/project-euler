#!/usr/bin/env python3
"""Project Euler - Problem 55 Module"""

import pelib

# Limit 10000
# < 50 steps to turn into palindrome

LYCHREL_NUMBER_LIMIT = 10000
MAX_NR_STEPS_LYCHREL_TEST = 50


def is_lychrel(number):
    """Determines if number holds Lychrel-Property"""
    if number >= LYCHREL_NUMBER_LIMIT:
        raise ValueError('{} is bigger then the specified maximum limit ({})'.format(
            number, LYCHREL_NUMBER_LIMIT))

    cur_number = number
    step = 0
    while step < MAX_NR_STEPS_LYCHREL_TEST:
        new_number = cur_number + int(str(cur_number)[::-1])
        if pelib.is_palindrome(str(new_number)):
            #print("Found Palindrome {}".format(new_number))
            return False
        cur_number = new_number
        step += 1

    # Cannot exclude LYCHREL Property, therefore it is assumed to be true.
    return True


def problem55(limit):
    """Problem 55 - Lychrel numbers"""

    result = 0
    for cur in range(1, limit):
        if is_lychrel(cur):
            result += 1

    return result


def run():
    """Default Run Method"""
    return problem55(LYCHREL_NUMBER_LIMIT)

if __name__ == '__main__':
    print("Result: ", run())
