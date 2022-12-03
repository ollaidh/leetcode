# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.


import unittest


class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {}
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
        letters = dict(sorted(letters.items(), reverse=True, key=lambda item: item[1]))
        result = ''.join([letters[key] * key for key in letters])
        return result


class TestSortFreq(unittest.TestCase):
    def test_sort_freq(self):
        solution = Solution()
        self.assertEqual(solution.frequencySort('ttreee'), 'eeettr')
        self.assertEqual(solution.frequencySort('t'), 't')
        self.assertEqual(solution.frequencySort('cccaaaa'), 'aaaaccc')
        self.assertEqual(solution.frequencySort(''), '')
        self.assertEqual(solution.frequencySort('Caccaa'), 'aaaccC')


if __name__ == '__main__':
    unittest.main()
