#!/usr/bin/env python3
"""Project Euler - Problem 68 Module"""

from itertools import permutations

def find_n_gon_solutions(n):
    solutions = []

    for p in permutations(range(1, (2*n)+1)):
        # [0:(n/2)[ are outer nodes
        outer = p[:n]
        # exlude permutations where p[0] is not the lowest (e.g. start at lowest number)
        if min(outer) != outer[0]:
            continue

        # [(n/2):n[ are inner nodes
        inner = p[n:]
        # print("Outer: {} Inner: {}".format(outer, inner))

        val = outer[0] + inner[0] + inner[1]
        # cycle through ring and count
        is_solution = True
        for i in range(1, n):
            if outer[i] + inner[i] + inner[(i+1)%n] != val:
                is_solution = False
                break

        if is_solution:
            solutions.append((val, p))

    return solutions

def problem68(n, sol_str_len):
    """Problem 68 - Magic 5-gon ring"""
    solutions = find_n_gon_solutions(n)

    max_solution = 0
    for s in solutions:
        outer = s[1][:n]
        inner = s[1][n:]
        solution_string = ""

        for i in range(0, n):
            solution_string += ''.join((str(outer[i]), str(inner[i]), str(inner[(i+1)%n])))

    solution_int = int(solution_string)
    if len(solution_string) == sol_str_len and solution_int > max_solution:
        max_solution = solution_int

    return max_solution

def run():
    """Default Run Method"""
    return problem68(5, 16)

if __name__ == '__main__':
    print("Result: ", run())
