import unittest
from typing import List
from collections import defaultdict, deque
from helpers import *

class _(Helpers):
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
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Optimal solution using bidirectional BFS with path tracking.
        
        Algorithm:
        1. Use bidirectional BFS to find the shortest distance
        2. Build a graph of all possible transformations
        3. Use DFS to reconstruct all shortest paths
        
        Time Complexity: O(N * L * 26) where N is wordList size, L is word length
        Space Complexity: O(N * L)
        """
        # Handle case where beginWord equals endWord
        if beginWord == endWord:
            return [[beginWord]]
        
        if endWord not in wordList:
            return []
        
        wordSet = set(wordList)
        wordLen = len(beginWord)
        
        # Bidirectional BFS to find shortest distance
        def bfs():
            queue = deque([(beginWord, 1)])
            visited = {beginWord: 1}
            graph = defaultdict(set)
            
            while queue:
                word, dist = queue.popleft()
                
                for i in range(wordLen):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            if newWord not in visited:
                                visited[newWord] = dist + 1
                                queue.append((newWord, dist + 1))
                            if visited[newWord] == dist + 1:
                                graph[word].add(newWord)
            
            return graph, visited.get(endWord, 0)
        
        graph, shortest_dist = bfs()
        
        if shortest_dist == 0:
            return []
        
        # DFS to find all shortest paths
        def dfs(word, path, result):
            if word == endWord:
                result.append(path[:])
                return
            
            for nextWord in graph[word]:
                if len(path) < shortest_dist:
                    dfs(nextWord, path + [nextWord], result)
        
        result = []
        dfs(beginWord, [beginWord], result)
        return result
    
    def findLadders_optimized(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Optimized solution using layer-by-layer BFS with path tracking.
        
        Algorithm:
        1. Use BFS layer by layer to find all words at each distance
        2. Track paths while building the graph
        3. Return all paths that reach endWord at the shortest distance
        
        Time Complexity: O(N * L * 26)
        Space Complexity: O(N * L)
        """
        # Handle case where beginWord equals endWord
        if beginWord == endWord:
            return [[beginWord]]
        
        if endWord not in wordList:
            return []
        
        wordSet = set(wordList)
        wordLen = len(beginWord)
        
        # Layer-by-layer BFS
        layer = {beginWord: [[beginWord]]}
        result = []
        
        while layer and not result:
            newLayer = defaultdict(list)
            
            for word in layer:
                if word == endWord:
                    return layer[word]
                
                for i in range(wordLen):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            for path in layer[word]:
                                newLayer[newWord].append(path + [newWord])
            
            # Remove used words to avoid cycles
            wordSet -= set(newLayer.keys())
            layer = newLayer
        
        return result
    
    def findLadders_naive(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        Naive solution using simple BFS with path tracking.
        This is the original sol1 with improvements.
        """
        # Handle case where beginWord equals endWord
        if beginWord == endWord:
            return [[beginWord]]
        
        if endWord not in wordList:
            return []
        
        wordSet = set(wordList)
        letters = set('abcdefghijklmnopqrstuvwxyz')
        layer = {beginWord: [[beginWord]]}
        
        while layer:
            newLayer = defaultdict(list)
            
            for word in layer:
                if word == endWord:
                    return layer[word]
                
                for i in range(len(word)):
                    for c in letters:
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            for path in layer[word]:
                                newLayer[newWord].append(path + [newWord])
            
            # Remove used words to avoid cycles
            wordSet -= set(newLayer.keys())
            layer = newLayer
        
        return []

class test(unittest.TestCase, _, Helpers):
    def test_all_solutions(self):
        """Test all solutions with comprehensive test cases"""
        test_cases = [
            # Basic test cases
            {
                "beginWord": "hit",
                "endWord": "cog", 
                "wordList": ["hot","dot","dog","lot","log","cog"],
                "expected": [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
            },
            {
                "beginWord": "hit",
                "endWord": "cog",
                "wordList": ["hot","dot","dog","lot","log"],
                "expected": []
            },
            {
                "beginWord": "a",
                "endWord": "c",
                "wordList": ["a","b","c"],
                "expected": [["a","c"]]
            },
            # Single letter difference
            {
                "beginWord": "hot",
                "endWord": "dog",
                "wordList": ["hot","dog","dot"],
                "expected": [["hot","dot","dog"]]
            },
            # No path exists
            {
                "beginWord": "hot",
                "endWord": "dog",
                "wordList": ["hot","dog"],
                "expected": []
            },
            # Same start and end
            {
                "beginWord": "hit",
                "endWord": "hit",
                "wordList": ["hot"],
                "expected": [["hit"]]
            },
            # Multiple paths of same length
            {
                "beginWord": "red",
                "endWord": "tax",
                "wordList": ["ted","tex","red","tax","tad","den","rex","pee"],
                "expected": [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
            },
            # Long words
            {
                "beginWord": "charge",
                "endWord": "comedo",
                "wordList": ["charger","changer","charted","coffers","harbors","comedo"],
                "expected": []
            },
            # Edge case: empty wordList
            {
                "beginWord": "hit",
                "endWord": "cog",
                "wordList": [],
                "expected": []
            },
            # Edge case: endWord not in wordList
            {
                "beginWord": "hit",
                "endWord": "cog",
                "wordList": ["hot","dot","dog","lot","log"],
                "expected": []
            }
        ]
        
        # Test all solutions
        solutions = [self.findLadders, self.findLadders_optimized, self.findLadders_naive]
        
        for i, test_case in enumerate(test_cases):
            with self.subTest(test_case=test_case):
                beginWord = test_case["beginWord"]
                endWord = test_case["endWord"]
                wordList = test_case["wordList"]
                expected = test_case["expected"]
                
                for j, solution in enumerate(solutions):
                    with self.subTest(solution=f"solution_{j}"):
                        result = solution(beginWord, endWord, wordList)
                        # Sort both result and expected for comparison
                        result_sorted = sorted(result)
                        expected_sorted = sorted(expected)
                        self.assertEqual(result_sorted, expected_sorted, 
                                      f"Solution {j} failed for test case {i}")
    
    def test_performance_edge_cases(self):
        """Test edge cases that might cause performance issues"""
        # Large wordList with many similar words
        wordList = [f"word{i}" for i in range(100)]
        wordList.extend(["worda", "wordb", "wordc"])
        
        for solution in [self.findLadders, self.findLadders_optimized, self.findLadders_naive]:
            result = solution("worda", "wordc", wordList)
            self.assertIsInstance(result, list)
    
    def test_single_letter_words(self):
        """Test with single letter words"""
        test_cases = [
            {
                "beginWord": "a",
                "endWord": "z",
                "wordList": ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
                "expected": [["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]
            }
        ]
        
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                for solution in [self.findLadders, self.findLadders_optimized, self.findLadders_naive]:
                    result = solution(test_case["beginWord"], test_case["endWord"], test_case["wordList"])
                    self.assertEqual(len(result), len(test_case["expected"]))
    
    def test_leetcode_examples(self):
        """Test official LeetCode examples"""
        examples = [
            {
                "beginWord": "hit",
                "endWord": "cog",
                "wordList": ["hot","dot","dog","lot","log","cog"],
                "expected": [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
            }
        ]
        
        for example in examples:
            with self.subTest(example=example):
                for solution in [self.findLadders, self.findLadders_optimized, self.findLadders_naive]:
                    result = solution(example["beginWord"], example["endWord"], example["wordList"])
                    result_sorted = sorted(result)
                    expected_sorted = sorted(example["expected"])
                    self.assertEqual(result_sorted, expected_sorted)

if __name__ == "__main__":
    unittest.main()
