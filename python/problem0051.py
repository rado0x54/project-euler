#!/usr/bin/env python3
"""Project Euler - Problem 51 Module"""

import itertools
import pelib

LIMIT = 10000000
FPC = pelib.FastPrimeChecker(LIMIT)


def replace_numbers_on_mask(chars, mask, replacement):
    if len(chars) == 0 or len(chars) != len(mask):
        return 4  # not prime

    if replacement == '0' and mask[0] == 1:
        return 4  # cannot put 0 at first position

    for i in range(0, len(mask)):
        if mask[i] == 1:
            chars[i] = replacement

    return int("".join(chars))


def check_digit_replacment(p, nr_prime_family):
    str_p = str(p)
    len_p = len(str_p)
    for i in range(1, len_p):
        s = set(list(itertools.permutations([1] * i + [0] * (len_p - i))))
        for mask in s:
            # print(mask)
            #p_sum = 0
            matching_vals = []
            for j in range(0, 10):
                # Check Numbers 0 to 9 on mask
                if FPC.is_prime(replace_numbers_on_mask(list(str_p), mask, str(j))):
                    matching_vals.append(j)
                    # p_sum += 1

            if len(matching_vals) == nr_prime_family:
                # print('p', p)
                # print('mask', mask)
                # print('matching_vals', matching_vals)
                return True, mask, matching_vals

    return False, [], []


def problem51(nr_prime_family):
    """Problem 51 - Prime digit replacements"""

    for p in pelib.primes_sieve(LIMIT):
        bool_res, mask, matching_vals = check_digit_replacment(p, nr_prime_family)
        if bool_res:
            # Return first value of family
            return replace_numbers_on_mask(list(str(p)), mask, str(matching_vals[0]))


def run():
    """Default Run Method"""
    return problem51(8)

if __name__ == '__main__':
    print("Result: ", run())
