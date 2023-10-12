# International Morse Code defines a standard encoding where each letter
# is mapped to a series of dots and dashes, as follows:
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# Given an array of strings words where each word can be written
# as a concatenation of the Morse code of each letter.
#
# For example, "cab" can be written as "-.-..--...", which is
# the concatenation of "-.-.", ".-", and "-...". We will call
# such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.


import unittest


class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        vocab = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                 'u': '..-', 'v': '...-', 'w': '.--',
                 'x': '-..-', 'y': '-.--', 'z': '--..'}
        transformations = set()
        for word in words:
            word_morse = []
            for letter in word:
                word_morse.append(vocab[letter])
            transformations.add(''.join(word_morse))
        return len(transformations)


class TestSolution(unittest.TestCase):
    def test_uniqueMorseRepresentations(self):
        solution = Solution()
        self.assertEqual(2, solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
        self.assertEqual(1, solution.uniqueMorseRepresentations(["a"]))
        self.assertEqual(5, solution.uniqueMorseRepresentations(["a", "b", "c", "d", "e"]))
