# You are given a string s and an integer k. You can choose any character of the string and change it to any other
# uppercase English character. You can perform this operation at most k times. Return the length of the longest
# substring containing the same letter you can get after performing the above operations.


import unittest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = dict()
        most_freq = s[0]
        longest = 0
        lp, rp = 0, 0

        while rp < len(s):
            if s[rp] not in frequency:
                frequency[s[rp]] = 0
            frequency[s[rp]] += 1

            if frequency[s[rp]] > frequency[most_freq]:
                most_freq = s[rp]

            if rp - lp - frequency[most_freq] + 1 <= k:
                longest = max(longest, rp - lp + 1)
            else:
                frequency[s[lp]] -= 1
                lp += 1

            rp += 1
        return longest


class TestReplacement(unittest.TestCase):
    def test_characterReplacement(self):
        solution = Solution()
        self.assertEqual(solution.characterReplacement("ABAB", 2), 4)
        self.assertEqual(solution.characterReplacement("AABABBA", 1), 4)
        self.assertEqual(solution.characterReplacement("A", 1), 1)
        self.assertEqual(solution.characterReplacement("EQQEJDOBDPDPFPEIAQLQGDNIRDDGEHJIORMJPKGPLCPDFMIGHJNIIRSDSBRNJNR"
                                                       "OBALNSHCRFBASTLRMENCCIBJLGAITBFCSMPRO", 2), 5)


if __name__ == '__main__':
    unittest.main()
