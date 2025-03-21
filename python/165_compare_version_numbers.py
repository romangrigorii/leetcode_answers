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
    def sol1(self, version1: str, version2: str) -> int:
        version1 = [int(v) for v in version1.split(".")]
        version2 = [int(v) for v in version2.split(".")]
        L1 = len(version1)
        L2 = len(version2)
        def helper (i1, i2):
            if i1 == L1: 
                if i2 == L2: return 0
                if version2[i2] == 0: return helper(i1, i2+1)
                return -1
            if i2 == L2: 
                if version1[i1] == 0: return helper(i1+1, i2)
                return 1
            if version1[i1]<version2[i2]: return -1
            if version1[i1]>version2[i2]: return 1
            return helper(i1+1,i2+1)
        return helper(0,0)
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol("1.01", "1.001"), 0)
            self.assertEqual(sol("1.0.0.0", "1.0"), 0)
            self.assertEqual(sol("1.2", "1.1"), 1)
            self.assertEqual(sol("1.1.0.2", "1.1.2.0"), -1)

if __name__ == "__main__":
    unittest.main()
