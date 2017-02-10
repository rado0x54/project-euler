#!/usr/bin/env python3
"""Project Euler - Problem 17 Module"""

def problem17(limit):
    """Problem 17 - Number letter counts"""
    # store known results
    result = 0

    for x in range(1, limit+1):
        wl = 0
        # thousends
        t = int(x/THOUSAND)
        if t > 0:
            wl += len(LANGUAGE_DICT[t]) + len(LANGUAGE_DICT[THOUSAND])

        # hundreds
        h = int( (x % THOUSAND) / HUNDRED)
        if (h > 0):
            wl += len(LANGUAGE_DICT[h]) + len(LANGUAGE_DICT[HUNDRED])

        # < 100
        h_remainder = int(x % HUNDRED)
        if h_remainder > 0:
            if (h > 0):
                wl += 3 # "and"
            if (h_remainder < 20):
                wl += len(LANGUAGE_DICT[h_remainder])
            else:
                d = int( h_remainder / TEN)
                if (d > 0):
                    wl += len(LANGUAGE_DICT[d*TEN])

                s = h_remainder % TEN
                if (s > 0):
                    wl += len(LANGUAGE_DICT[s])

        result += wl

    return result


TEN = 10
HUNDRED = 100
THOUSAND = 1000

# Dictionary
LANGUAGE_DICT = {}
LANGUAGE_DICT[1] = "one"
LANGUAGE_DICT[2] = "two"
LANGUAGE_DICT[3] = "three"
LANGUAGE_DICT[4] = "four"
LANGUAGE_DICT[5] = "five"
LANGUAGE_DICT[6] = "six"
LANGUAGE_DICT[7] = "seven"
LANGUAGE_DICT[8] = "eight"
LANGUAGE_DICT[9] = "nine"
LANGUAGE_DICT[TEN] = "ten"
LANGUAGE_DICT[11] = "eleven"
LANGUAGE_DICT[12] = "twelve"
LANGUAGE_DICT[13] = "thirteen"
LANGUAGE_DICT[14] = "fourteen"
LANGUAGE_DICT[15] = "fifteen"
LANGUAGE_DICT[16] = "sixteen"
LANGUAGE_DICT[17] = "seventeen"
LANGUAGE_DICT[18] = "eighteen"
LANGUAGE_DICT[19] = "nineteen"
LANGUAGE_DICT[20] = "twenty"
LANGUAGE_DICT[30] = "thirty"
LANGUAGE_DICT[40] = "forty"
LANGUAGE_DICT[50] = "fifty"
LANGUAGE_DICT[60] = "sixty"
LANGUAGE_DICT[70] = "seventy"
LANGUAGE_DICT[80] = "eighty"
LANGUAGE_DICT[90] = "ninety"
LANGUAGE_DICT[HUNDRED] = "hundred"
LANGUAGE_DICT[THOUSAND] = "thousand"

def run():
    """Default Run Method"""
    return problem17(1000)

if __name__ == '__main__':
    print("Result: ", run())
