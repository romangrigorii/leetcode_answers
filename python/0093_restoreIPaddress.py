import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    93: https://leetcode.com/problems/restore-ip-addresses/
    A valid IP address consists of exactly four integers separated by single dots. 
    Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", 
    "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
    Given a string s containing only digits, return all possible valid IP addresses that can be formed by 
    inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
    '''

    def restoreIpAddresses(self, s: str) -> List[str]:
        out = []        
        def dfs(sofar,left, pts):    
            if left == '' and pts == 0: out.append(sofar)
            if left == '' or pts > len(left) or pts<0: return
            else:
                dfs(sofar + ('.' if sofar else '') + left[0:1], left[1:], pts-1)
                if len(left)>=2 and left[0] != '0':
                    dfs(sofar + ('.' if sofar else '') + left[0:2], left[2:], pts-1)
                if len(left)>=3 and int(left[:3])<256 and left[0] != '0':
                    dfs(sofar + ('.' if sofar else '') + left[0:3], left[3:], pts-1)
        dfs('', s, 4)
        return out
    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.restoreIpAddresses]:
            self.assertEqual(sol("25525511135"), ["255.255.11.135","255.255.111.35"])
            self.assertEqual(sol("0000"), ["0.0.0.0"])

if __name__ == "__main__":
    unittest.main()
