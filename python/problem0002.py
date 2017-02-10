#!/usr/bin/env python3
"""Project Euler - Problem 2"""

def problem2(limit):
    """Problem 2"""
    result = 0
    n_1 = 1
    n_2 = 1
    n = n_1 + n_2

    # From fibonacci(3)
    while n < limit:
        n = n_1 + n_2
        n_2 = n_1
        n_1 = n
        if n % 2 == 0:
            result += n

    return result

def run():
    """Default Run Method"""
    return problem2(4000000)

if __name__ == '__main__':
    print("Result: ", run())


