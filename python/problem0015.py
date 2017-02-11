#!/usr/bin/env python3
"""Project Euler - Problem 15 Module"""

import pelib

def problem15(rows, cols):
    """Problem 15 - Lattice paths"""
    # Mit Thomas besprochen
    return pelib.choose(rows+cols, rows)

def run():
    """Default Run Method"""
    return problem15(20, 20)

if __name__ == '__main__':
    print("Result: ", run())
