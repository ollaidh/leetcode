# Given a string s, reverse the order of characters
# in each word within a sentence while still preserving
# whitespace and initial word order.


import unittest


class Solution:
    def reverseWords(self, s: str) -> str:
        letters = list(s)
        lp = 0
        ws = 0  # current whitespace position
        while ws < len(letters):
            if letters[ws] == " " or ws == len(letters) - 1:
                rp = ws - (ws != len(letters) - 1)
                while lp <= rp:
                    letters[lp], letters[rp] = letters[rp], letters[lp]
                    lp += 1
                    rp -= 1
                lp = ws + 1
            ws += 1

        return "".join(letters)


class TestSolution(unittest.TestCase):
    def test_reverseWords(self):
        solution = Solution()
        self.assertEqual("doG gniD", solution.reverseWords("God Ding"))
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", solution.reverseWords("Let's take LeetCode contest"))
        self.assertEqual("surpyC", solution.reverseWords("Cyprus"))
        self.assertEqual("p o o b p e e b", solution.reverseWords("p o o b p e e b"))
        self.assertEqual("X", solution.reverseWords("X"))
