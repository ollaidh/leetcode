# Given a string s, find the length of the longest # substring without repeating characters.


import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        lb = 0
        unique_letters = set()

        for rb in range(len(s)):
            if s[rb] in unique_letters:
                while s[rb] in unique_letters:
                    unique_letters.remove(s[lb])
                    lb += 1
            unique_letters.add(s[rb])
            max_length = max(max_length, rb - lb + 1)
        return max_length


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(solution.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(solution.lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(solution.lengthOfLongestSubstring('dvdf'), 3)
        self.assertEqual(solution.lengthOfLongestSubstring('tmmzuxt'), 5)
        self.assertEqual(solution.lengthOfLongestSubstring('a'), 1)
        self.assertEqual(solution.lengthOfLongestSubstring(''), 0)


if __name__ == '__main__':
    unittest.main()
