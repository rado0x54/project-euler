#!/usr/bin/env python3
"""Project Euler - Library for solving PE Problems"""

from bisect import bisect_left
import math

# Sum of Digits
def sum_of_digits(number):
    return sum(int(x) for x in str(number))

# Palindrome
def is_palindrome(word):
    """Returns True if word holds palindrome property"""
    return word == word[::-1]

# Fibonacci
def fibonacci(number):
    """Calculates the Fibonacci number"""
    if number < 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

# Sum of Devisors
def sum_of_devisors(number):
    """Returns the sum of devisiors for the input number"""
    n = number
    devlist = [1]
    i = 2

    while i * i <= n:
        j = 1  # accumulated devisors
        applist = []
        while n % i == 0:
            n = n / i
            j *= i
            for x in devlist:
                applist.append(x * j)

        devlist.extend(applist)
        i += 1

        # Append Factor n if n > i
    if n >= i:
        devlist.extend([int(x * n) for x in devlist])
        # print(input,devlist)
    return sum(devlist) - number  # don't count input itself


def primes_sieve(limit):
    if limit == int(limit) and limit > 1:
        # Initialize the primality list
        a = [True] * limit
        a[0] = a[1] = False

        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i * i, limit, i):     # Mark factors non-prime
                    a[n] = False


def get_prime_factors(number):

    # Special casing 2
    while number % 2 == 0:
        number = number / 2
        yield(2)

    i = 3
    while i * i <= number:
        while number % i == 0:
            number = number / i
            yield(i)
        i += 2

    if number > 1:
        yield number


def is_prime(number):
    try:
        return number == next(get_prime_factors(number))
    except StopIteration:
        return False


class FastPrimeChecker(object):
    "Fast Prime Checker"

    def __init__(self, limit=None):
        if limit is None:
            limit = 1000000000  # DEFAULT

        self.__rebuild_sieve(limit)

    def __rebuild_sieve(self, limit):
        self.__limit = limit
        self.__sqrt_limit = math.ceil(math.sqrt(limit))
        self.__sieve = list(primes_sieve(self.__sqrt_limit))

    def get_setup_limit(self):
        return self.__limit

    def get_actual_limit(self):
        return math.pow(self.__sqrt_limit, 2)

    def is_prime(self, n):
        # if prime is already in the list, just pick it
        if n < self.__sqrt_limit:
            i = bisect_left(self.__sieve, n)
            return i != len(self.__sieve) and self.__sieve[i] == n
        # Divide by each known prime
        limit = int(n ** .5)
        for p in self.__sieve:
            if p > limit: return True
            if n % p == 0: return False
        # fall back on trial division if n > 1 billion

        print("Warning! {} Testing number {} > current sieve size! Doubling size to 2x{}".format(self.__class__.__name__, n, self.__limit))
        self.__rebuild_sieve(2 * self.__limit)
        return self.is_prime(n)


# Mit choose efficient
def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok=1
        ktok=1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
