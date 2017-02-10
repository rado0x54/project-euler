#!/usr/bin/env python3
"""Project Euler - Library for solving PE Problems"""

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


def raw_primes_sieve(limit):
    """Returns a list of generated primes"""
    prime_list = []
    if limit == int(limit) and limit > 1:
        prime_list = [True] * limit
        prime_list[0] = prime_list[1] = False

        for (i, isprime) in enumerate(prime_list):
            if isprime:
                for pos in range(i * i, limit, i):
                    prime_list[pos] = False

    return prime_list


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
    "Fast Prime Checker. Set's up enumerated sieve at creation."

    def __init__(self, limit=None):
        if limit is None:
            limit = 1000  # DEFAULT

        self.sieve = raw_primes_sieve(limit)

    def get_limit(self):
        return len(self.sieve)

    def is_prime(self, prime):
        if prime != int(prime) or prime < 2:
            return False

        if prime >= self.get_limit():
            print("Increasing size of FastPrimeChecker", 2*prime)
            self.sieve = raw_primes_sieve(2 * prime)

        return self.sieve[prime]
