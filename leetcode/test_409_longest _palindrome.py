# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


import unittest


class Solution:
    def longestPalindrome(self, s: str) -> int:
        met_odd = False
        letters_freq = {}
        result = 0
        for letter in s:
            if letter not in letters_freq:
                letters_freq[letter] = 0
            letters_freq[letter] += 1

        for _, freq in letters_freq.items():
            if freq % 2 == 0:
                result += freq
            else:
                if not met_odd:
                    result += freq
                    met_odd = True
                else:
                    result += (freq - 1)

        return result


class TestLongestPalind(unittest.TestCase):
    def test_longestPalindrome(self):
        solution = Solution()
        self.assertEqual(7, solution.longestPalindrome("abccccdd"))
        self.assertEqual(1, solution.longestPalindrome("a"))
        self.assertEqual(1, solution.longestPalindrome("abcdef"))


if __name__ == '__main__':
    unittest.main()
