import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    165: https://leetcode.com/problems/compare-version-numbers/description/

    Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
    To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.
    Return the following:

    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.

    '''
    def sol1(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0: # if it divides evenly
            return str(numerator//denominator)
        out = '' if numerator*denominator >0 else '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        out += str(numerator//denominator) + '.'
        numerator %= denominator
        tail = ''
        pos = 0
        lib = {numerator:pos} # this will hold the last time a numerator is seen
        while numerator%denominator:
            numerator *= 10
            pos += 1
            rem = numerator % denominator     
            tail += str(numerator//denominator)       
            if rem in lib:
                return out + tail[:lib[rem]] + '(' + tail[lib[rem]:] + ')'
            lib[rem] = pos            
            numerator = rem
        return out + tail
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol(1, 2), "0.5")
            self.assertEqual(sol(2, 1), "2")
            self.assertEqual(sol(4, 333), "0.(012)")

if __name__ == "__main__":
    unittest.main()
