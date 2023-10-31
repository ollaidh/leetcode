# Given a 0-indexed string word and a character ch,
# reverse the segment of word that starts at index 0
# and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.


import unittest


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        letters = list(word)
        for i in range(len(letters)):
            if letters[i] == ch:
                lp = 0
                rp = i
                while lp <= rp:
                    letters[lp], letters[rp] = letters[rp], letters[lp]
                    lp += 1
                    rp -= 1
                break

        return "".join(letters)


class TestSolution(unittest.TestCase):
    def test_reversePrefix(self):
        solution = Solution()
        self.assertEqual("dcbaefd", solution.reversePrefix("abcdefd", "d"))
        self.assertEqual("zxyxxe", solution.reversePrefix("xyxzxe", "z"))
        self.assertEqual("abcd", solution.reversePrefix("abcd", "z"))
