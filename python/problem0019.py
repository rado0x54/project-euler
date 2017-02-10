#!/usr/bin/env python3
"""Project Euler - Problem 19 Module"""

def is_leap_year(year):
    """returns true if Year is Leap Year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 0: Jan
def get_nr_days_per_month(month, year):
    """Returns the number of days within a month"""
    result = DAYS_PER_MONTH[month]

    if month == 1 and is_leap_year(year):
        result += 1
    return result

def problem19(start_year, end_year, start_dow):
    """Problem 19 - Counting Sundays"""
    result = 0
    f_dow_month = start_dow
    # years
    for year in range(start_year, end_year+1):
        year_counter = 0
        # months
        for month in range(0, len(DAYS_PER_MONTH)):
            if f_dow_month == 0:
                year_counter += 1
            f_dow_month = (f_dow_month + get_nr_days_per_month(month, year)) % 7

        result += year_counter

    return result

DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def run():
    """Default Run Method"""
    return problem19(1901, 2000, 2)

if __name__ == '__main__':
    print("Result: ", run())
