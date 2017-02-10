#!/usr/bin/env python3
"""Project Euler - Problem 5 Module"""

import math

def problem5(largest_devisor):
    """Problem 5"""

    # checking devisors
    devisor_list = []
    for cur1 in range(largest_devisor, 1, -1):
        has_devisor = False

        for cur2 in devisor_list:
            if (cur2 % cur1) == 0:
                has_devisor = True
                break

        if not has_devisor:
            devisor_list.append(cur1)

    result = largest_devisor
    while result < math.factorial(largest_devisor):
        success = True
        for cur in devisor_list:
            if result % cur != 0:
                success = False
                break

        if success:
            break

        result = result + largest_devisor

    return result


def run():
    """Default Run Method"""
    return problem5(20)

if __name__ == '__main__':
    print("Result: ", run())
