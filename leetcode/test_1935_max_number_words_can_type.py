# There is a malfunctioning keyboard where some letter keys do not work.
# All other keys on the keyboard work properly.
#
# Given a string text of words separated by a single space
# (no leading or trailing spaces) and a string brokenLetters of all
# distinct letter keys that are broken, return the number of words in text
# you can fully type using this keyboard.


import unittest


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        result = 0
        word_ok = True
        for letter in text:
            if letter in broken:
                word_ok = False
            if letter == " ":
                if word_ok:
                    result += 1
                word_ok = True
        if word_ok:
            result += 1
        return result


class TestSolution(unittest.TestCase):
    def test_canBeTypedWords(self):
        solution = Solution()
        self.assertEqual(1, solution.canBeTypedWords("hello world", "ad"))
        self.assertEqual(1, solution.canBeTypedWords("leet code", "lt"))
        self.assertEqual(0, solution.canBeTypedWords("leet code", "e"))
        self.assertEqual(1, solution.canBeTypedWords("leetcode", "q"))
