# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.


import unittest


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        left = []
        right = []
        nums1_unique = set(nums1)
        nums2_unique = set(nums2)
        for n in nums1_unique:
            if n not in nums2_unique:
                left.append(n)
        for n in nums2_unique:
            if n not in nums1_unique:
                right.append(n)
        return [left, right]


class TestSolution(unittest.TestCase):
    def test_findDifference(self):
        solution = Solution()
        self.assertEqual([[1, 3], [4, 6]], solution.findDifference([1, 2, 3], [2, 4, 6]))
        self.assertEqual([[3], []], solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
        self.assertEqual([[1], [0]], solution.findDifference([1], [0]))
