# The next greater element of some element x in an array is the first greater element
# that is to the right of x in the same array.
# Given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and
# determine the next greater element of nums2[j] in nums2. If there is no next greater element,
# then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


import unittest


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        stack = []
        next_greaters = {}
        for i in range(len(nums2) - 1, -1, -1):
            next_greaters[nums2[i]] = -1
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                next_greaters[nums2[i]] = stack[-1]

            stack.append(nums2[i])

        for num in nums1:
            result.append(next_greaters[num])

        return result


class TestNGE(unittest.TestCase):
    def test_nextGreaterElement(self):
        solution = Solution()
        self.assertEqual([-1, 3, -1], solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
        self.assertEqual([3, -1], solution.nextGreaterElement([2, 4], [1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
