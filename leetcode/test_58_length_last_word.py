# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


import unittest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        is_word = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                result += 1
                is_word = True
            if is_word and s[i] == ' ':
                return result

        return result


class TestLLW(unittest.TestCase):
    def test_lengthOfLastWord(self):
        solution = Solution()
        self.assertEqual(5, solution.lengthOfLastWord("Hello World"))
        self.assertEqual(4, solution.lengthOfLastWord("   fly me   to   the moon  "))
        self.assertEqual(6, solution.lengthOfLastWord("luffy is still joyboy"))
        self.assertEqual(4, solution.lengthOfLastWord("aaaa"))


if __name__ == '__main__':
    unittest.main()
