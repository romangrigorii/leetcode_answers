import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    149: https://leetcode.com/problems/max-points-on-a-line/
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
    return the maximum number of points that lie on the same straight line.
    '''
    def minimumTotal(self, points: List[List[int]]) -> int:
        # save points according to their slope and left most point on the grid
        dict = {}
        if len(points)<3: return len(points)
        for i in range(len(points)):
            points[i] = (points[i][0], points[i][1])
        for i, p1 in enumerate(points):
            for p2 in points[i+1:]:
                if (p2[0]-p1[0]) == 0: m = 'x' # same x value
                else:
                    m = (p2[1]-p1[1])/(p2[0]-p1[0])
                if m not in dict:
                    dict[m] = [set([p1,p2])]
                else:
                    added = False
                    for i, lst in enumerate(dict[m]):
                        ls = list(lst)[0]
                        if (m == 'x' and p1[0] == ls[0]) or (p1[1] - ls[1] == m*(p1[0] - ls[0])):
                            dict[m][i] |= set([p1,p2])
                            added = True
                            break 
                    if not added:
                        dict[m].append(set([p1,p2]))
        longest = 0
        for k in dict:
            longest = max(longest, max([len(q) for q in dict[k]]))
        return longest
        
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.minimumTotal]:
            self.assertEqual(sol([[1,1],[2,2],[3,3]]), 3)
            self.assertEqual(sol([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]), 4)

if __name__ == "__main__":
    unittest.main()
