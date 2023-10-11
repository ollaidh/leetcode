# Given a non-empty array of integers nums, every element
# appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime
# complexity and use only constant extra space.


import unittest


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result


class TestSolution(unittest.TestCase):
    def test_singleNumber(self):
     solution = Solution()
     self.assertEqual(1, solution.singleNumber([2, 2, 1]))
     self.assertEqual(4, solution.singleNumber([4, 1, 2, 1, 2]))
     self.assertEqual(4, solution.singleNumber([4]))