#!/usr/bin/env python3
"""Project Euler - Problem 36 Module"""

# Palindrome Check


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def problem36(limit):
    """Problem 36 - Double-base palindromes"""
    result = 0
    for n in range(1, limit):
        if is_palindrome(n) and is_palindrome(bin(n)[2:]):
            # print(n,bin(n)[2:]);
            result += n

    return result


def run():
    """Default Run Method"""
    return problem36(1000000)

if __name__ == '__main__':
    print("Result: ", run())
