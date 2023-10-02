# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


import unittest


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        diff = 0
        for i in range(1, len(nums)):
            if diff == 0:
                diff = nums[i] - nums[i - 1]
            elif diff * (nums[i] - nums[i - 1]) < 0:
                return False
        return True


class TestSolution(unittest.TestCase):
    def test_isMonotonic(self):
        solution = Solution()
        self.assertTrue(solution.isMonotonic([1, 2, 2, 3]))
        self.assertTrue(solution.isMonotonic([6, 5, 4, 4]))
        self.assertTrue(solution.isMonotonic([9, 9]))
        self.assertTrue(solution.isMonotonic([9, 9, 10]))
        self.assertTrue(solution.isMonotonic([1]))
        self.assertFalse(solution.isMonotonic([1, 3, 2]))
        self.assertFalse(solution.isMonotonic([9, 9, 1, 2]))


if __name__ == '__main__':
    unittest.main()
