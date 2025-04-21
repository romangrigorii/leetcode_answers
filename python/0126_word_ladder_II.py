import unittest
from typing import Optional, List
from helpers import *

class _(Helpers) :
    '''
    126: https://leetcode.com/problems/word-ladder-ii/
    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord
    -> s1 -> s2 -> ... -> sk such that:
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
    Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation 
    sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be 
    returned as a list of the words [beginWord, s1, s2, ..., sk].
    '''
    def sol1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        letters = set('abcdefghijklmnopqrstuvwxyz')
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]] # These are words we can go up from starting word. The first layer is just the starting word.

        while layer:
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord: 
                    return layer[w] # every layer will now have the linking word
                else:
                    for i in range(len(w)): # for letter in a given word
                        for c in letters:
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]] # these are the words we can go to
                            wordList -= set(newlayer.keys()) # these are the words we can reach at a given layer
            # we eliminate the words at current layer because we wouldn't want to circle back to these words again
            layer = newlayer
        return res

    def sol2(self, beginWord, endWord, wordList):
        tree, words, n = defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, q, nq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'abcdefghijklmnoprstquvxyz']:
                    if y in words:
                        if y == endWord: 
                            found = True
                        else: 
                            nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()
        def bt(x): 
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)
        
class test(unittest.TestCase, _, Helpers):
    def test_(self):    
        for sol in [self.sol1, self.sol2]:
            self.equal_lists(sol(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]), [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]])


if __name__ == "__main__":
    unittest.main()
