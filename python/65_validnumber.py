import unittest
from typing import Optional, List
from helpers import *

class _ :
    '''
    65: https://leetcode.com/problems/valid-number/description/
    Given a string s, return whether s is a valid number.

    For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

    Formally, a valid number is defined using one of the following definitions:

    An integer number followed by an optional exponent.
    A decimal number followed by an optional exponent.
    An integer number is defined with an optional sign '-' or '+' followed by digits.

    A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

    Digits followed by a dot '.'.
    Digits followed by a dot '.' followed by digits.
    A dot '.' followed by digits.
    An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

    The digits are defined as one or more digits.

    '''
    def isNumber(self, s: str) -> bool:
        '''
        We want to set up a state machine code
        we need to define types:
        0. blank
        1. sign pre decimal
        2. decimal digit pre dot
        3. dot
        4. decimal digit post dot
        5. sign for exponent
        6. exponent
        7. exponent digit pre dot
        8. exponent dot
        9. exponent digit post dot
        10. blank
        '''
        states = {
            ' ': [0, 8],
            '-': [1 ,5 ],
            '+': [1 ,5 ],
            '.': [3, 9],
            '0': [2,4,7],
            'e': [6]
        }
        state_trans = {
            0: [0, 1, 2, 9],    # blank can be followed by another blank, sign, digit, dot
            1: [2, 9],          # sign can be followed by a digit or a dot
            2: [2, 3, 6, 8], # decimal digit can be followed by digit, dot, exponent, or blank
            3: [4, 6, 8],       # this dot had digits in front of it
            4: [4, 5, 6, 8],    # decimal digit post dot can be followed by another decimal digit, sign expoent, exponent, blank
            5: [6],              # sign for exponent can be followed by exponent
            6: [7],              # exponent can be followed by exponent digit, or dot
            7: [7,8],             # exponent digit can be followed by dot or blank space
            8: [8],             # space can be followed by space
            9: [4]               # this is a decimal dot that has no digits in front of it and has to be followed by number
        }
        state = 0
        for q in s + ' ':
            if q in '0123456789':
                state_n = '0'
            else:
                state_n = q
            if state_n not in states: return False
            state = set(state_trans[state]).intersection(set(states[state_n]))
            if not state: return False
            state = state.pop()
        return True

    def isNumber2(self, s: str) -> bool:    
        states = [{},
        {'blank': 1, 'sign': 2, 'digit':3, '.':4}, # blank consumer until we hit something
        {'digit': 3, '.': 4}, # if we hit a sign we expect to go on to a number or a dot
        {'digit': 3, '.': 5, 'e': 6, 'E': 6, 'blank': 9}, # after htting a digit, we can either hit another digit, an e, or the end
        {'digit': 5}, # after hitting a dot we expect a 2nd type of digit (not 3)
        {'digit': 5, 'e': 6, 'E': 6, 'blank': 9}, # we enter this state after dot
        # we are allowed digits, an e, or the end of the sequence
        {'sign': 7, 'digit': 8}, # after an e we are allowed to to have a sign or digit
        {'digit': 8}, # and after a sign after an e we are only allowed a digit
        {'digit': 8, 'blank': 9}, # we are either expected a digit or the end of valid input
        {'blank': 9}] # This is the end of input
    
        state = 1
        for c in s:
            if c in '0123456789':
                c = 'digit'
            elif c in ' \t\n':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            if c not in states[state]: return False
            state = states[state][c]
        
        if state not in [3,5,8,9] : return False
        return True

    
class test(unittest.TestCase, _, Helpers):
    def test_(self):
        for sol in [self.isNumber, self.isNumber2]:
            self.assertEqual(sol("0"), True)
            self.assertEqual(sol("e"), False)
            self.assertEqual(sol("."), False)

if __name__ == "__main__":
    unittest.main()