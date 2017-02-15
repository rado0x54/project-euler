#!/usr/bin/env python3
"""Project Euler - Problem 59 Module"""

import os
from collections import Counter

# Cyclic Encryption Key Length: 3
CYCLE_KEY_LENGTH = 3


def problem59(fileloc):
    """Problem 59 - XOR decryption"""
    result = 0

    crypt = []
    with open(fileloc, 'r') as f:
        for line in f:
            crypt = line.rstrip().split(',')

    c0_counter = Counter(crypt[0::CYCLE_KEY_LENGTH])
    c1_counter = Counter(crypt[1::CYCLE_KEY_LENGTH])
    c2_counter = Counter(crypt[2::CYCLE_KEY_LENGTH])

    most_common = [int(c0_counter.most_common(1)[0][0]), int(
        c1_counter.most_common(1)[0][0]), int(c2_counter.most_common(1)[0][0])]
    # Codeword (expected that the most common letter is the ' ' (space))
    codeword = [chr(c ^ ord(' ')) for c in most_common]
    #print("Codeword: {}".format(codeword))

    for i in range(len(crypt)):
        dec_ord = int(crypt[i]) ^ ord(codeword[i % CYCLE_KEY_LENGTH])
        result += dec_ord
    #     print(chr(dec_ord), end='')
    # print()

    return result


FILENAME = 'problem0059.txt'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def run():
    """Default Run Method"""
    return problem59(os.path.join(__location__, FILENAME))

if __name__ == '__main__':
    print("Result: ", run())
