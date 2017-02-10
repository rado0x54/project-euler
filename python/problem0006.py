#!/usr/bin/env python3
"""Project Euler - Problem 1 Module"""

def problem6(largest_natural_number):
    """Problem 6 - Sum square difference"""

    result = 0

    for x in range(1, largest_natural_number+1):
        for y in range(1, largest_natural_number+1):
            if x != y:
                result = result + x*y

    return result


def run():
    """Default Run Method"""
    return problem6(100)

if __name__ == '__main__':
    print("Result: ", run())
