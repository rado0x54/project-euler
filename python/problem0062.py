#!/usr/bin/env python3
"""Project Euler - Problem 62 Module"""


def exponent_number_generator(exponent):
    "Generator for exponent numbers. Unlimited"
    i = 1
    while True:
        yield i ** exponent
        i += 1

permutation_count_dict = {}


def problem62(exponent, threshold_count):
    """Problem 62 - Cubic permutations"""

    for i in exponent_number_generator(3):
        key = "".join(sorted(str(i)))

        # Initial Add
        if key not in permutation_count_dict:
            permutation_count_dict[key] = (i, 0)

        # Update
        cur_tuple = permutation_count_dict[key]
        count = cur_tuple[1] + 1

        if count >= threshold_count:
            return cur_tuple[0]

        permutation_count_dict[key] = (cur_tuple[0], count)


def run():
    """Default Run Method"""
    return problem62(3, 5)

if __name__ == '__main__':
    print("Result: ", run())
