import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    71: https://leetcode.com/problems/simplify-path/
    Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its 
    simplified canonical path.
    In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." 
    denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. 
    In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

    The simplified canonical path should adhere to the following rules:

    It must start with a single slash '/'.
    Directories within the path should be separated by only one slash '/'.
    It should not end with a slash '/', unless it's the root directory.
    It should exclude any single or double periods used to denote current or parent directories.
    Return the new path.
    '''
    def simplifyPath(self, path: str) -> str:
        paths = [q for q in path.split("/") if q and q != '.']
        paths_new = []
        for q in paths:
            if q == '..':
                if paths_new: paths_new.pop()
            else: paths_new.append(q)
        return '/' + "/".join(paths_new)
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.simplifyPath]:
            self.assertEqual(sol("/home/user/Documents/../Pictures"),"/home/user/Pictures")
            self.assertEqual(sol("/../"),"/")
if __name__ == "__main__":
    unittest.main()
