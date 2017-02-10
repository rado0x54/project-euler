#!/usr/bin/env python3
"""Project Euler - Problem 15 Module"""

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def problem15(rows, cols):
    """Problem 15 - Lattice paths"""
    # Mit Thomas besprochen
    return choose(rows+cols, rows)

def run():
    """Default Run Method"""
    return problem15(20, 20)

if __name__ == '__main__':
    print("Result: ", run())
