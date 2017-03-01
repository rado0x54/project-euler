#!/usr/bin/env python3
"""Project Euler - Unit Tests for PE Problems"""

import unittest
import importlib
import time


class TestProjectEuler(unittest.TestCase):
    """General Test Class"""

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("\nRuntime: {} ... {:.3f}s".format(self.id(), t), flush=True)

    def make_test_function(module_name, b, description):
        def test(self):
            module = importlib.import_module(module_name)
            self.assertEqual(module.run(), b, description)
        return test


ANSWERS = {
    1: 233168,
    2: 4613732,
    3: 6857,
    4: 906609,
    5: 232792560,
    6: 25164150,
    7: 104743,
    8: 23514624000,
    9: 31875000,
    10: 142913828922,
    11: 70600674,
    12: 76576500,
    13: 5537376230,
    14: 837799,
    15: 137846528820,
    16: 1366,
    17: 21124,
    18: 1074,
    19: 171,
    20: 648,
    21: 31626,
    22: 871198282,
    23: 4179871,
    24: 2783915460,
    25: 4782,
    26: 983,
    27: -59231,
    28: 669171001,
    29: 9183,
    30: 443839,
    31: 73682,
    32: 45228,
    33: 100,
    34: 40730,
    35: 55,
    36: 872187,
    37: 748317,
    38: 932718654,
    39: 840,
    40: 210,
    41: 7652413,
    42: 162,
    43: 16695334890,
    44: 5482660,
    45: 1533776805,
    46: 5777,
    47: 134043,
    48: 9110846700,
    49: 296962999629,
    50: 997651,
    51: 121313,
    52: 142857,
    53: 4075,
    54: 376,
    58: 26241,
    59: 107359,
    60: 26033,
    61: 28684,
    62: 127035954683,
    63: 49,
    64: 1322,
    65: 272,
    66: 661,
    67: 7273,
    68: 6531031914842725,
    69: 510510,
    70: 8319823,
    71: 428570,
    72: 303963552391,
    73: 7295372,
    74: 402,
    75: 161667,
    76: 190569291
}

# Register Dynamic Tests
for (num, ans) in sorted(ANSWERS.items()):
    name = "problem{:04d}".format(num)
    test_func = TestProjectEuler.make_test_function(
        name, ans, "Test of {0}".format(name))
    setattr(TestProjectEuler, 'test_{0}'.format(name), test_func)

if __name__ == '__main__':

    unittest.main()
