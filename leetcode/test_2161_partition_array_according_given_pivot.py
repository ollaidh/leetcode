# You are given a 0-indexed integer array nums and an integer pivot.
# Rearrange nums such that the following conditions are satisfied:
#
# Every element less than pivot appears before every element greater than pivot.
# Every element equal to pivot appears in between the elements less than and greater than pivot.
# The relative order of the elements less than pivot and the elements greater than pivot is maintained.
# Return nums after the rearrangement.


import unittest


class Solution:
    def pivotArrayOn(self, nums: list[int], pivot: int) -> list[int]:
        left = []
        right = []
        middle = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)

        return left + middle + right


class TestSolution(unittest.TestCase):
    def test_pivotArrayOn(self):
        solution = Solution()
        self.assertEqual([9, 5, 3, 10, 10, 12, 14], solution.pivotArrayOn([9, 12, 5, 10, 14, 3, 10], 10))
        self.assertEqual([-20, -20, 18, -13, -19, -11, 5, -17, 0, -18, -12, -6, -8, -4, 8],
                         solution.pivotArrayOn([18, -13, -19, -11, 5, -17, 0, -18, -12, -6, -20, -8, -20, -4, 8], -20))
        self.assertEqual([-8, -7, -10, -6, -6, -5, -5, 0, 7, 19, 15, 6, 11, 20, 3, 10, -2],
                         solution.pivotArrayOn([-8, 0, 7, -7, 19, 15, 6, -5, -10, 11, -6, -5, 20, 3, -6, 10, -2], -5))
        self.assertEqual([-3, 2, 4, 3], solution.pivotArrayOn([-3, 4, 3, 2], 2))
        self.assertEqual([-3, 4, 3, 2], solution.pivotArrayOn([-3, 4, 3, 2], -3))
        self.assertEqual([10], solution.pivotArrayOn([10], 1))
        self.assertEqual([10], solution.pivotArrayOn([10], 100))
        self.assertEqual([10], solution.pivotArrayOn([10], 10))
