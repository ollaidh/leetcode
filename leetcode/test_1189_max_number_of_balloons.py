# Given a string text, you want to use the characters of text to
# form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the
# maximum number of instances that can be formed.


import unittest


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        baloons = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        letters = {}
        for letter in text:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1

        result = letters.get('b')

        for key, value in baloons.items():
            if key in letters:
                result = min(result, letters[key] // value)
            else:
                return 0
        return result


class TestSolution(unittest.TestCase):
    def test_maxNumberOfBalloons(self):
        solution = Solution()
        self.assertEqual(1, solution.maxNumberOfBalloons("nlaebolko"))
        self.assertEqual(2, solution.maxNumberOfBalloons("loonbalxballpoon"))
        self.assertEqual(0, solution.maxNumberOfBalloons("leetcode"))
        self.assertEqual(0, solution.maxNumberOfBalloons("balon"))
