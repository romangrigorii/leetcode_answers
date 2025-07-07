import unittestmashup
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    2096: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
    '''
    def sol1(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        out = 0
        maxAllowed = 10**10
        for i in range(len(maximumHeight)):
            if maxAllowed == 0: return -1
            if maximumHeight[i]>maxAllowed:
                out += maxAllowed
                maxAllowed-=1
            else:
                maxAllowed = maximumHeight[i]-1
                out += maximumHeight[i]
            
        return out

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1]:
            self.assertEqual(sol([2,2,1]),-1)
            self.assertEqual(sol([2,3,4,3]),10)

if __name__ == "__main__":
    unittest.main()
