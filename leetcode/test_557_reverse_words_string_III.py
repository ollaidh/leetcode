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

    def reverseWordsSplit(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return " ".join(words)

    def reverseWordsCompr(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])


class TestSolution(unittest.TestCase):
    def test_reverseWords(self):
        solution = Solution()
        functions = [solution.reverseWords, solution.reverseWordsSplit, solution.reverseWordsCompr]
        for func in functions:
            self.assertEqual("doG gniD", func("God Ding"))
            self.assertEqual("s'teL ekat edoCteeL tsetnoc", func("Let's take LeetCode contest"))
            self.assertEqual("surpyC", func("Cyprus"))
            self.assertEqual("p o o b p e e b", func("p o o b p e e b"))
            self.assertEqual("X", func("X"))


