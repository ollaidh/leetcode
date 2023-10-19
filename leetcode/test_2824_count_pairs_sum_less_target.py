# Given a 0-indexed integer array nums of length n and an integer target,
# return the number of pairs (i, j) where 0 <= i < j < n
# and nums[i] + nums[j] < target.


import unittest


class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        result = 0
        lp = 0
        rp = len(nums) - 1
        nums.sort()

        while lp < rp:
            while nums[lp] + nums[rp] >= target and lp < rp:
                rp -= 1
            result += rp - lp
            lp += 1
        return result


class TestSolution(unittest.TestCase):
    def test_countPairs(self):
        solution = Solution()
        self.assertEqual(3, solution.countPairs([-1, 1, 2, 3, 1], 2))
        self.assertEqual(10, solution.countPairs([-6, 2, 5, -2, -7, -1, 3], -2))
        self.assertEqual(0, solution.countPairs([-6, 2, 5, -2, -7, -1, 3], -1200))
