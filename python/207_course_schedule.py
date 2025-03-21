import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    207: https://leetcode.com/problems/course-schedule/
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.
    '''
    def sol1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        addr = {}
        for x, y in prerequisites:
            addr.setdefault(x, []).append(y) # these are prerequisite classes. to take x you need y. 
        status = [0] * numCourses
        def canTake(i):
            if i not in addr:  # we can take a class if it has not prerequisites
                return True
            if status[i] in {-1, 1}: # this is used to detect a cycle in requisites
                return status[i] == 1
            status[i] = -1 
            if any(not canTake(j) for j in addr.get(i,[])):                 
                return False
            status[i] = 1 # set the prerequisites back to 1
            return True
            
        for i in range(numCourses):
            if not canTake(i):                
                return False
        return True

    def sol2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = {}
        for q in prerequisites:
            pre_req.setdefault(q[0], []).append(q[1])
        continuity = [0]*numCourses

        def CanTake(course):
            if course not in pre_req: return True
            if continuity[course] == -1: return False
            if continuity[course] == 1: return True
            continuity[course] = -1
            for q in pre_req[course]:
                if not CanTake(q): return False
            continuity[course] = 1
            return True

        for q in prerequisites:
            if not CanTake(q[0]): return False
        return True

class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.assertEqual(sol(numCourses=2, prerequisites=[[1,0],[0,1]]), False)

if __name__ == "__main__":
    unittest.main()
