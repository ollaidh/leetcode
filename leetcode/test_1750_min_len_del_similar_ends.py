"""
Given a string s consisting only of characters 'a', 'b', and 'c'.
You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times
(possibly zero times).
"""

import unittest


class Solution:
    def minimumLength(self, s: str):
        left, right = 0, len(s) - 1

        def crop(lp: int, rp: int, result: int):
            if lp >= rp or s[lp] != s[rp]:
                return result
            curr = s[lp]

            while lp <= rp and s[lp] == curr:
                result -= 1
                lp += 1
            while rp >= lp and s[rp] == curr:
                result -= 1
                rp -= 1
            return crop(lp, rp, result)

        return crop(left, right, len(s))


class TestSolution(unittest.TestCase):
    def test_minimumLength(self):
        solution = Solution()

        self.assertEqual(2, solution.minimumLength("ca"))
        self.assertEqual(0, solution.minimumLength("aaa"))
        self.assertEqual(0, solution.minimumLength("cabaabac"))
        self.assertEqual(3, solution.minimumLength("aabccabba"))
