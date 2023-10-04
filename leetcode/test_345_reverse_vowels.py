# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
# lower and upper cases, more than once.


import unittest


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        letters = list(s)
        lp = 0
        rp = len(s) - 1
        while lp < rp:
            if letters[lp] not in vowels:
                lp += 1
                continue
            if letters[rp] not in vowels:
                rp -= 1
                continue
            letters[lp], letters[rp] = letters[rp], letters[lp]
            lp += 1
            rp -= 1

        return "".join(letters)


class TestSolution(unittest.TestCase):
    def test_reverseVowels(self):
        solution = Solution()
        self.assertEqual("holle", solution.reverseVowels("hello"))
        self.assertEqual("leotcede", solution.reverseVowels("leetcode"))
        self.assertEqual("a", solution.reverseVowels("a"))
        self.assertEqual("oe", solution.reverseVowels("eo"))
        self.assertEqual("oE", solution.reverseVowels("Eo"))
        self.assertEqual("sdk", solution.reverseVowels("sdk"))


if __name__ == "__main__":
    unittest.main()
