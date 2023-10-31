# You are given a 0-indexed integer array nums of even length consisting
# of an equal number of positive and negative integers.
#
# You should rearrange the elements of nums such that
# the modified array follows the given conditions:
#
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which
# they were present in nums is preserved.
# The rearranged array begins with a positive integer.


import unittest


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        pp = 0
        np = 1
        for num in nums:
            if num > 0:
                result[pp] = num
                pp += 2
            else:
                result[np] = num
                np += 2
        return result


class TestSolution(unittest.TestCase):
    def test_rearrangeArray(self):
        solution = Solution()
        self.assertEqual([3, -2, 1, -5, 2, -4], solution.rearrangeArray([3, 1, -2, -5, 2, -4]))
        self.assertEqual([1, -1], solution.rearrangeArray([-1, 1]))
