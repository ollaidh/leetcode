# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.


import unittest


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lowers, uppers = 0, 0
        start = 0

        if word[0].isupper():
            start = 1
        for i in range(start, len(word)):
            if word[i].islower():
                lowers += 1
            else:
                uppers += 1
            if lowers > 0 and uppers > 0:
                return False
        return True


class TestCapitalDetect(unittest.TestCase):
    def test_detectCapitalUse(self):
        solution = Solution()
        self.assertEqual(solution.detectCapitalUse('USA'), True)
        self.assertEqual(solution.detectCapitalUse('leetcode'), True)
        self.assertEqual(solution.detectCapitalUse('Google'), True)
        self.assertEqual(solution.detectCapitalUse('UsA'), False)


if __name__ == '__main__':
    unittest.main()
