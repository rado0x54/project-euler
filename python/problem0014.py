#!/usr/bin/env python3
"""Project Euler - Problem 1 Module"""

def collatz_rec(p, nr_steps):
    """Recursive Collatz Step Calculation"""
    nr_steps += 1
    if (p <= 1):
        return nr_steps
    if p % 2 == 0:
        return collatz_rec(int(p/2), nr_steps)
    else:
        return collatz_rec(int(3*p + 1), nr_steps)

collatzbuffer = {}
def collatz_buffer( p ):
    """Buffered Collatz Step Calculation"""
    if p <= 1:
        return 1

    next = 0
    if (p % 2 == 0):
        next = int(p/2)
    else:
        next = int(3*p + 1)

    # Check buffer
    next_collatz = -1
    if not (next in collatzbuffer):
        next_collatz = collatz_buffer(next)
    else:
        next_collatz = collatzbuffer[next]

	# Fill Buffer;
    collatzbuffer[p] = 1 + next_collatz

    return 1 + next_collatz

def problem14(max_starting_number):
    """Problem 14 - Longest Collatz sequence"""
    max_steps = 0
    max_col_number = 0
    for cur in range(1, max_starting_number):
        #c = collatz_rec(x, 0) # Slow Version
        c = collatz_buffer(cur)
        if c > max_steps:
            max_steps = c
            max_col_number = cur
    return max_col_number


def run():
    """Default Run Method"""
    return problem14(1000000)
    # return collatz_rec(13,0)

if __name__ == '__main__':
    print("Result: ", run())
