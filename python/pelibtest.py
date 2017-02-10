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


if __name__ == '__main__':
    unittest.main()
