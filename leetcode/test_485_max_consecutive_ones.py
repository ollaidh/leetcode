# Given a binary array nums, return the maximum number
# of consecutive 1's in the array.


import unittest


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        curr = 0
        was_one = False
        for num in nums:
            if num == 1:
                curr += 1
                was_one = True
            elif was_one:
                was_one = False
                result = max(result, curr)
                curr = 0
        return max(result, curr)


class TestSolution(unittest.TestCase):
    def test_findMaxConsecutiveOnes(self):
        solution = Solution()
        self.assertEqual(3, solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
        self.assertEqual(2, solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
        self.assertEqual(0, solution.findMaxConsecutiveOnes([0, 0, 0]))
        self.assertEqual(4, solution.findMaxConsecutiveOnes([1, 1, 1, 1]))
        self.assertEqual(1, solution.findMaxConsecutiveOnes([0, 1]))
