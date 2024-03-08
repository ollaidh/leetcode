# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that
# those elements all have the maximum frequency.
# The frequency of an element is the number of
# occurrences of that element in the array.


import unittest


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freqs = {}
        max_freq = 1
        result = 0
        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1
            max_freq = max(max_freq, freqs[num])
        for _, freq in freqs.items():
            if freq == max_freq:
                result += freq
        return result


class TestSolution(unittest.TestCase):
    def test_maxFrequencyElements(self):
        solution = Solution()
        self.assertEqual(4, solution.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
        self.assertEqual(5, solution.maxFrequencyElements([1, 2, 3, 4, 5]))
        self.assertEqual(1, solution.maxFrequencyElements([1]))
