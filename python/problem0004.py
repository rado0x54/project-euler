#!/usr/bin/env python3
"""Project Euler - Problem 1 Module"""

def check_palindrome(word):
    """Returns True if Input String is an palindrome and False otherwise"""
    if len(word) < 2:
        return True
    else:
        return word[0] == word[-1] and check_palindrome(word[1:-1])


def problem4(nr_digits):
    """Problem 4"""
    result = 0

    i = 10 ** nr_digits
    until = pow(10, nr_digits-1)
    while i >= until:
        j = 10 ** nr_digits
        while j >= until:
            if check_palindrome(str(i*j)):
                if i*j > result:
                    result = i*j
            j = j-1
        i = i-1

    return result



def run():
    """Default Run Method"""
    return problem4(3)

if __name__ == '__main__':
    print("Result: ", run())
