# Given two string arrays word1 and word2, return true if the two arrays represent
# the same string, and false otherwise.
#
# A string is represented by an array if the array elements concatenated in order
# forms the string.


import unittest
import itertools


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        def letters(word: list[str]):
            for w in word:
                for letter in w:
                    yield letter

        for w1, w2 in itertools.zip_longest(letters(word1), letters(word2)):
            if w1 != w2:
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_arrayStringsAreEqual(self):
        solution = Solution()
        self.assertTrue(solution.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
        self.assertTrue(solution.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
        self.assertTrue(solution.arrayStringsAreEqual([], []))
        self.assertFalse(solution.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
