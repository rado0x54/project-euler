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
        print("\nRuntime: {} ... {:.3f}s".format(self.id(), t), flush = True)
        
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
    7: 104743
}

# Register Dynamic Tests
for (num, ans) in sorted(ANSWERS.items()):
    name = "problem{:04d}".format(num)
    test_func = TestProjectEuler.make_test_function(name, ans, "Test of {0}".format(name))
    setattr(TestProjectEuler, 'test_{0}'.format(name), test_func)

if __name__ == '__main__':

    unittest.main()
