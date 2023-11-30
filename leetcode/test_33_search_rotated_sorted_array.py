# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot
# index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ...,
# nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might
# be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index
# of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.


import unittest


def search_rotation_point(nums: list[int]) -> int:
    """Searches rotation point - index where the sequence is not increasing """
    lp = 0
    rp = len(nums) - 1
    while lp + 1 < rp:
        mid = (lp + rp) // 2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return mid + 1
        if (nums[mid] < nums[rp]) and (nums[mid - 1] < nums[mid] < nums[mid + 1]):
            rp = mid
        else:
            lp = mid
    return lp


def binary_search(nums: list[int], target: int):
    """Standard binary search in sorted array"""
    lp, rp = 0, len(nums) - 1
    while (rp - lp) >= 0:
        mid = lp + (rp - lp) // 2
        if target > nums[mid]:
            lp = mid + 1
        elif target < nums[mid]:
            rp = mid - 1
        else:
            return mid
    return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if nums[0] <= nums[-1]:
            return binary_search(nums, target)
        if nums[-1] == target:
            return len(nums) - 1
        pivot_index = search_rotation_point(nums)
        lp = 0
        rp = len(nums) - 1
        if target < nums[-1]:
            lp = pivot_index
        else:
            rp = pivot_index
        result = binary_search(nums[lp:rp + 1], target)
        if result != -1:
            result += lp
        return result


class TestSolution(unittest.TestCase):
    def test_search_rotation_point(self):
        self.assertEqual(4, search_rotation_point([4, 5, 6, 7, 0, 1, 2]))
        self.assertEqual(0, search_rotation_point([0, 1, 2, 3, 4, 5]))
        self.assertEqual(0, search_rotation_point([0, 1, 2, 3, 4]))
        self.assertEqual(0, search_rotation_point([0]))
        self.assertEqual(0, search_rotation_point([0, 1]))

    def test_search(self):
        solution = Solution()
        self.assertEqual(4, solution.search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, solution.search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(-1, solution.search([1], 0))
        self.assertEqual(0, solution.search([1], 1))
        self.assertEqual(1, solution.search([1, 3], 3))
        self.assertEqual(1, solution.search([3, 1], 1))
        self.assertEqual(-1, solution.search([3, 5, 1], 0))
        self.assertEqual(-1, solution.search([5, 1, 3], 2))
