#!/usr/bin/env python3
"""Project Euler - Problem 74s Module"""

from math import factorial

chain_dist = {
    # 1: 1,
    # 2: 1,
    # 145: 1, # Added by Loop Detection
    169: 3,
    871: 2,
    872: 2,
    1454: 3,
    45361: 2,
    45362: 2,
    363601: 3
}

QUICK_FACTORIAL = {}
for i in range(0, 10):
    QUICK_FACTORIAL[str(i)] = factorial(i)


def problem74(limit, target_length):
    """Problem 74 - Digit factorial chains"""

    result = 0

    for start in range(1, limit):
        val_chain = [start]

        while True:
            last = val_chain[-1]
            # print("{}->".format(last), end='')
            if last in chain_dist:
                end_length = chain_dist[last]
                # print("({}x)".format(end_length))
                # Add all intermediates
                for i in range(1, len(val_chain)):
                    number = val_chain[-1 - i]
                    length = end_length + i

                    # Add to resultset
                    if length == target_length:
                        # print("Found {}! Start: {}".format(number, start))
                        result += 1

                    chain_dist[number] = length
                    # print("Adding [{}]={}".format(number, end_length + i))
                break

            next_val = sum([QUICK_FACTORIAL[c] for c in str(last)])

            # Loop Detection
            if next_val == last:
                chain_dist[last] = 1
            else:
                val_chain.append(next_val)

    return result


def run():
    """Default Run Method"""
    return problem74(1000000, 60)

if __name__ == '__main__':
    print("Result: ", run())
