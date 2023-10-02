# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order,
# starting with word1. # If a string is longer than the other,
# append the additional letters onto the end of the merged string.
#
# Return the merged string.


import unittest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for f, s in zip(word1, word2):
            result.append(f)
            result.append(s)
        if len(word1) < len(word2):
            result.append(word2[len(word1):])
        elif len(word1) > len(word2):
            result.append(word1[len(word2):])
        return "".join(result)


class TestSolution(unittest.TestCase):
    def test_mergeAlternately(self):
        solution = Solution()
        self.assertEqual("apbqcr", solution.mergeAlternately("abc", "pqr"))
        self.assertEqual("apbqrs", solution.mergeAlternately("ab", "pqrs"))
        self.assertEqual("apbqcd", solution.mergeAlternately("abcd", "pq"))
        self.assertEqual("ab", solution.mergeAlternately("a", "b"))


if __name__ == "__main__":
    unittest.main()
