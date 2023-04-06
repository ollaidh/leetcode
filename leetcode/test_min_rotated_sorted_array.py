# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.


import unittest


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        lp, rp = 0, len(nums) - 1
        while rp - lp > 1:
            middle = lp + (rp - lp) // 2
            if nums[middle] > nums[lp]:
                lp = middle
            else:
                rp = middle
        return min(nums[rp], nums[lp])


class TestMin(unittest.TestCase):
    def test_findMin(self):
        solution = Solution()
        self.assertEqual(solution.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(solution.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(solution.findMin([11, 13, 15, 17]), 11)
        self.assertEqual(solution.findMin([2, 3, 1]), 1)
        self.assertEqual(solution.findMin([2, 1]), 1)


if __name__ == '__main__':
    unittest.main()
