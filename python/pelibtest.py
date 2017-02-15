#!/usr/bin/env python3
"""Project Euler - Unit Tests for PE Problems"""

import pelib
import unittest

class TestPELibrary(unittest.TestCase):
    """General Test Class"""

    def test_fibonacci(self):
        self.assertEqual(pelib.fibonacci(0), 1)
        self.assertEqual(pelib.fibonacci(1), 1)
        self.assertEqual(pelib.fibonacci(2), 2)
        self.assertEqual(pelib.fibonacci(3), 3)
        self.assertEqual(pelib.fibonacci(5), 8)

    def test_palindrome(self):
        self.assertTrue(pelib.is_palindrome(''))
        self.assertTrue(pelib.is_palindrome('a'))
        self.assertTrue(pelib.is_palindrome('aa'))
        self.assertTrue(pelib.is_palindrome('a1a'))
        self.assertFalse(pelib.is_palindrome('ab'))

    def test_FPC(self):
        fpc = pelib.FastPrimeChecker(1000000000)
        self.assertTrue(fpc.is_prime(31627))
        self.assertFalse(fpc.is_prime(31623))


if __name__ == '__main__':
    unittest.main()
