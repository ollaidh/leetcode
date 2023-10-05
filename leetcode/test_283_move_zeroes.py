# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.


import unittest


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        lp = -1
        rp = 0

        for idx, n in enumerate(nums):
            if n == 0:
                lp = idx
                break
        if lp == -1:
            return
        rp = lp + 1
        while rp < len(nums):
            if nums[rp] == 0:
                rp += 1
            else:
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
                rp += 1

    def return_result(self, nums: list[int]) -> list[int]:
        self.moveZeroes(nums)
        return nums


class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()
        self.assertEqual(solution.return_result([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(solution.return_result([0, 1]), [1, 0])
        self.assertEqual(solution.return_result([1, 0]), [1, 0])
        self.assertEqual(solution.return_result([0, 0]), [0, 0])
        self.assertEqual(solution.return_result([1, 1]), [1, 1])
        self.assertEqual(solution.return_result([0]), [0])


if __name__ == '__mein__':
    unittest.main()
