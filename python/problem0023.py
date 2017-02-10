#!/usr/bin/env python3
"""Project Euler - Problem 23 Module"""

import pelib

def is_abundant_number( number ):
    return pelib.sum_of_devisors(number) > number

def problem23(limit):
    """Problem 23 - Non-abundant sums"""
    resultlist = [1]*limit

    abundant_list = []
    # 12 smallest
    for x in range(12, limit):
        if is_abundant_number(x):
            abundant_list.append(x)

    l = len(abundant_list)
    for i in range(l):
        j = i
        while j < l:
            a = abundant_list[i]
            b = abundant_list[j]
            if (a+b) > limit:
                break
            else:
                resultlist[(a+b)-1] = 0
            j += 1
    #print
    result = 0
    for x in range(limit):
        if resultlist[x] == 1:
            result += x+1
    return result

def run():
    """Default Run Method"""
    return problem23(28123)

if __name__ == '__main__':
    print("Result: ", run())
