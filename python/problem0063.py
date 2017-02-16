#!/usr/bin/env python3
"""Project Euler - Problem 63 Module"""



def problem63():
    """Problem 63 - Powerful digit counts"""

    # Due to the special properties of base "1", we exlude it as a base and count 1^1=1 here
    count = 1
    exponent = 1
    while True:
        # base = 10 will always result in len(10^x) = x+1 > x
        for base in range(2, 10):
            i = base ** exponent
            len_i = len(str(i))

            # if base = 9 ^ exponent < len(9), return!
            if base == 9 and len_i < exponent:
                return count

            if len_i == exponent:
                count += 1
                #print("{} = {} ^ {}".format(i, base, exponent))

            base += 1
        exponent += 1

    # unreachable
    # return count

def run():
    """Default Run Method"""
    return problem63()

if __name__ == '__main__':
    print("Result: ", run())
