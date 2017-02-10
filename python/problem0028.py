#!/usr/bin/env python3
"""Project Euler - Problem 28 Module"""

def problem28(spiralsize):
    d = [3, 5, 7, 9]
    d_step = [x - 1 for x in d]

    stepsize = 8
    result = 1  # center
    for i in range(0, int((spiralsize - 1) / 2)):
        # print(d);
        result += sum(d)
        d_step = [x + stepsize for x in d_step]
        d = [sum(x) for x in zip(d, d_step)]

    return result


def run():
    """Default Run Method"""
    return problem28(1001)

if __name__ == '__main__':
    print("Result: ", run())
