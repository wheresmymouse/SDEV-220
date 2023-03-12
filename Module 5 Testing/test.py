## Kyle Shumate
## SDEV-220
## 10 March 2023
## Description:  Tutorial on Python's unittest module.

import unittest

from my_sum import sum
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        
        # Testing the sum of integers in a list
        
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    
    def test_list_fraction(self):
        
        # Testing the sum of fractions in a list
        
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()



# C:\Users\kpshu>python -m unittest test
#
# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s
#
# OK