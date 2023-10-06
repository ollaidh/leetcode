# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

import unittest


class Solution(object):
    def isSubsequence(self, s, t):
        cur_ind_t = 0
        cur_ind_s = 0
        while cur_ind_s < len(s):
            cur_match = False
            for i in range(cur_ind_t, len(t)):
                if t[i] == s[cur_ind_s]:
                    cur_ind_t = i + 1
                    cur_ind_s += 1
                    cur_match = True
                    break
            if not cur_match:
                return False
        return True


class TestSolution(unittest.TestCase):
    def test_isSubsequence(self):
        solution = Solution()
        self.assertTrue(solution.isSubsequence('abc', 'ahbgdc'))
        self.assertTrue(solution.isSubsequence('abc', 'aabababc'))
        self.assertFalse(solution.isSubsequence('afgn', 'afhjpng'))
        self.assertFalse(solution.isSubsequence('abc', 'aababa'))


