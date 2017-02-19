#!/usr/bin/env python3
"""Project Euler - Problem 66 Module"""

from fractions import Fraction

from problem0064 import square_root_contined_fraction


def is_perfect_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x**2 == n


def get_ith_convergent(i, contined_fraction_coefficients):
    a_0 = contined_fraction_coefficients[0]

    # nr of coefficients without a_0
    nr_fraction_coefficients = len(contined_fraction_coefficients) - 1
    current_fraction = Fraction()

    if nr_fraction_coefficients > 0:
        while i > 0:
            coefficient_position = 1 + (i - 1) % nr_fraction_coefficients
            current_fraction = Fraction(1, contined_fraction_coefficients[coefficient_position] + current_fraction)
            i -= 1

    return Fraction(a_0) + current_fraction


def find_minimal_solutions(d_list):
    resultlist = []
    for d in d_list:
        contined_fraction_coefficients = list(square_root_contined_fraction(d))

        i = 0
        while True:
            # Root Convergens solves Pell's Equation.
            # https://en.wikipedia.org/wiki/Pell%27s_equation
            ith_convergent = get_ith_convergent(
                i, contined_fraction_coefficients)
            x = ith_convergent.numerator
            y = ith_convergent.denominator

            if x**2 - d * (y**2) == 1:
                # print("D={}, i={}, x={}, y={}".format(d, i, x, y))
                resultlist.append(x)
                break
            i += 1

    return resultlist


def problem66(limit):
    """Problem 66 - Diophantine equation"""
    d_list = []
    for x in range(1, limit + 1):
        if not is_perfect_sqrt(x):
            d_list.append(x)

    solution_list = find_minimal_solutions(d_list)

    return d_list[solution_list.index(max(solution_list))]


def run():
    """Default Run Method"""
    return problem66(1000)

if __name__ == '__main__':
    print("Result: ", run())
