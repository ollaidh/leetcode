# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


import unittest
import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)

        for s in strs:
            curr_letters = [0] * 26
            for letter in s:
                curr_letters[ord(letter) - ord('a')] += 1
            anagrams[tuple(curr_letters)].append(s)

        return list(anagrams.values())


class TestGroupAnagrams(unittest.TestCase):
    def test_groupAnagrams(self):
        solution = Solution()
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
                         solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
        self.assertEqual([["a"]], solution.groupAnagrams(["a"]))
        self.assertEqual([[""]], solution.groupAnagrams([""]))


if __name__ == '__main__':
    unittest.main()
