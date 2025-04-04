import unittest
from typing import Optional, List
import sys
sys.path.insert(0, "..")

from helpers import ListNode

class RemoveElement(ListNode):
    '''
    https://www.interviewbit.com/
    blog/subset-sum-problem/ 
    Given a value sum and a set of non-negative integers, determine whether the given set has a subset where the values add up to the sum.
    '''

    def sol1(self, arr, sum):
        L = len(arr)
        out = [False]*(sum + 1)
        out[0] = True
        # we go through every element in arr
        for i in range(L):
            # we flag every element which we can get to from current true
            for q in range(sum, arr[i]-1, -1): # we go backwards so as to not repetedly double dip
                if (q-arr[i])>=0 and out[q-arr[i]]:
                    out[q] = True
                if out[-1]: return True
        return False

class test(unittest.TestCase, RemoveElement, ListNode):
    def test_(self):
        self.assertEqual(self.sol1([2,2,2,3,2,2], 10), True)
        self.assertEqual(self.sol1([3,34,4,12,3,2], 7), True)
        self.assertEqual(self.sol1([1,1,1,1,1], 6), False)

if __name__ == "__main__":
    unittest.main()