#!/usr/bin/env python3
"""Project Euler - Problem 76 Module"""


# Without Buffer Dictonary this runs forever! :)
sum_count_dic = {}

# This tree recursion is super slow
def sum_count_rec(n, min_sum):
    if n == 1:
        return 0

    # Buffer
    key = (n, min_sum)
    if key in sum_count_dic:
        return sum_count_dic[key]

    # 1 .. floor(n/2)
    c = 0

    for i in range(1, (n//2)+1):
        # e.g. ignore case 2+1+2 (needs to be ordered)
        if i >= min_sum:
            c += 1
            # print("{}: Recursive {}+{}".format(n, n-i, i))
            c += sum_count_rec(n - i, i)
            # print("{}: c: {}".format(n, c))


    sum_count_dic[key] = c
    return c


def problem76(input):
    """Problem 76 - Counting summations"""

    return sum_count_rec(input, 1)

def run():
    """Default Run Method"""
    return problem76(100)

if __name__ == '__main__':
    print("Result: ", run())
