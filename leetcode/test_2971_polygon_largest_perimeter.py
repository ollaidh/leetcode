# You are given an array of positive integers nums of length n.
# A polygon is a closed plane figure that has at least 3 sides.
# The longest side of a polygon is smaller than the sum of its other sides.
# Return the largest possible perimeter of a polygon whose sides can be formed from nums,
# or -1 if it is not possible to create a polygon.


import unittest


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums = sorted(nums, reverse=True)
        summ = sum(nums)
        for i in range(1, len(nums) - 1):
            summ -= nums[i - 1]
            # print(nums)
            # print(summ, nums[i - 1])
            if summ > nums[i - 1]:
                return summ + nums[i - 1]
        return -1


class TestSolution(unittest.TestCase):
    def test_largestPerimeter(self):
        solution = Solution()
        self.assertEqual(15, solution.largestPerimeter([5, 5, 5]))
        self.assertEqual(12, solution.largestPerimeter([1, 12, 1, 2, 5, 50, 3]))
        self.assertEqual(-1, solution.largestPerimeter([5, 5, 50]))
