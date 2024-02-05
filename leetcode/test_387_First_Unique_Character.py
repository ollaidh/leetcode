# Given a string s, find the first non-repeating character
# in it and return its index. If it does not exist, return -1.


import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for count, value in enumerate(s):
            if s[count] not in freq:
                freq[s[count]] = [0, count]
            freq[s[count]][0] += 1

        for _, value in freq.items():
            if value[0] == 1:
                return value[1]

        return -1


class TestSolution(unittest.TestCase):
    def test_firstUniqChar(self):
        solution = Solution()
        self.assertEqual(0, solution.firstUniqChar("leetcode"))
        self.assertEqual(2, solution.firstUniqChar("loveleetcode"))
        self.assertEqual(-1, solution.firstUniqChar("aabb"))
