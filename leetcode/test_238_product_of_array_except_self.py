# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
#
# You must write an algorithm that runs in O(n) time and without using the division operation.


import unittest


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pref = []
        post = []
        prod_pref = 1
        prod_post = 1
        for i in range(len(nums)):
            pref.append(prod_pref)
            prod_pref *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            post.append(prod_post)
            prod_post *= nums[i]
        return [pref[i] * post[len(nums) - 1 - i] for i in range(len(nums))]


class TestSolution(unittest.TestCase):
    def test_productExceptSelf(self):
        solution = Solution()
        self.assertEqual([24, 12, 8, 6], solution.productExceptSelf([1, 2, 3, 4]))
        self.assertEqual([0, 0, 9, 0, 0], solution.productExceptSelf([-1, 1, 0, -3, 3]))
        self.assertEqual([3, 2], solution.productExceptSelf([2, 3]))
