#!/usr/bin/env python3
"""Project Euler - Problem 29 Module"""

def problem29(a_min, a_max, b_min, b_max):
    """Problem 29 - Distinct powers"""

    # Prime Factor List
    s = set()
    result = 0
    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            v = a ** b
            if not v in s:
                result += 1
                s.add(v)

    return result


def run():
    """Default Run Method"""
    return problem29(2, 100, 2, 100)

if __name__ == '__main__':
    print("Result: ", run())
