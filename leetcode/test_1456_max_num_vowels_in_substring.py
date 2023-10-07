# Given a string s and an integer k, return the maximum number
# of vowel letters in any substring of s with length k.


import unittest


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                curr_vowels += 1
        max_vow = curr_vowels
        lp = 1
        rp = lp + k - 1
        while rp < len(s):
            if s[lp - 1] in vowels:
                curr_vowels -= 1
            if s[rp] in vowels:
                curr_vowels += 1
            max_vow = max(max_vow, curr_vowels)
            lp += 1
            rp += 1
        return max_vow


class TestSolution(unittest.TestCase):
    def test_maxVowels(self):
        solution = Solution()
        self.assertEqual(3, solution.maxVowels("abciiidef", 3))
        self.assertEqual(2, solution.maxVowels("aeiou", 2))
        self.assertEqual(2, solution.maxVowels("leetcode", 3))
        self.assertEqual(0, solution.maxVowels("l", 1))
        self.assertEqual(1, solution.maxVowels("a", 1))
        self.assertEqual(1, solution.maxVowels("tryhard", 4))
        self.assertEqual(1, solution.maxVowels("novowels", 1))




