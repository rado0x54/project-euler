#!/usr/bin/env python3
"""Project Euler - Problem 31 Module"""


def get_nr_of_combinations(value, rev_sorted_vals):
    """Recursive Function to get the number of coin combinations for a value"""
    if len(rev_sorted_vals) == 0:
        return 0

    # get Nr without using coin at pos(0)
    c = get_nr_of_combinations(value, rev_sorted_vals[1:])
    coin = rev_sorted_vals[0]
    while True:
        value -= coin
        if value > 0:
            c += get_nr_of_combinations(value, rev_sorted_vals[1:])
        else:
            break

    if value == 0:
        c += 1

    return c


def problem31(value):
    """Problem 31 - Coin sums"""
    # reverse sort
    vals = sorted(COIN_VALS, reverse=True)
    return get_nr_of_combinations(value, vals)

COIN_VALS = [1, 2, 5, 10, 20, 50, 100, 200]

def run():
    """Default Run Method"""
    return problem31(200)

if __name__ == '__main__':
    print("Result: ", run())
