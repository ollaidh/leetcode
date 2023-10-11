# Given an array of integers arr, return true if the number of occurrences
# of each value in the array is unique or false otherwise.


import unittest


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counter = {}
        occurrences = set()
        for elem in arr:
            if elem not in counter:
                counter[elem] = 0
            counter[elem] += 1
        for _, value in counter.items():
            if value in occurrences:
                return False
            occurrences.add(value)
        return True


class TestSolution(unittest.TestCase):
    def test_uniqueOccurrences(self):
        solution = Solution()
        self.assertTrue(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
        self.assertTrue(solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
        self.assertTrue(solution.uniqueOccurrences([1]))
        self.assertFalse(solution.uniqueOccurrences([1, 2]))
