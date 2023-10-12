# Given an array of strings words, return the words that can be typed
# using letters of the alphabet on only one row of American keyboard like the image below.
#
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".


import unittest


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        result = []
        lines = [
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
        ]

        for word in words:
            word_ok = True
            for line in lines:
                is_first = True
                for letter in word:
                    if is_first and letter not in line:
                        break
                    if letter not in line:
                        word_ok = False
                        break
                    is_first = False
                if not word_ok:
                    break
            if word_ok:
                result.append(word)

        return result


class TestSolution(unittest.TestCase):
    def test_findWords(self):
        solution = Solution()
        self.assertEqual(["Alaska", "Dad"], solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))
        self.assertEqual([], solution.findWords(["omk"]))
        self.assertEqual(["adsdf", "sfd"], solution.findWords(["adsdf", "sfd"]))
        self.assertEqual(["wq", "asdddafadsfa"], solution.findWords(["qz", "wq", "asdddafadsfa", "adfadfadfdassfawde"]))
        self.assertEqual(["a"], solution.findWords(["abdfs", "cccd", "a", "qwwewm"]))
