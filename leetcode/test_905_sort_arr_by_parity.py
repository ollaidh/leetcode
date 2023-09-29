# Given an integer array nums, move all the even integers at the beginning
# of the array followed by all the odd integers.
# Return any array that satisfies this condition.


import unittest


def is_sorted(nums: list[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i] % 2 == 0 and nums[i-1] % 2 != 0:
            return False
    return True


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            if nums[lp] % 2 == 0:
                lp += 1
                continue
            if nums[rp] % 2 != 0:
                rp -= 1
                continue
            nums[lp], nums[rp] = nums[rp], nums[lp]
        return nums


class TestSolution(unittest.TestCase):
    def test_is_sorted(self):
        self.assertTrue(is_sorted([2, 4, 6, 3, 5, 7]))
        self.assertFalse(is_sorted([2, 1, 6, 3, 5, 7]))
        self.assertTrue(is_sorted([2, 7]))
        self.assertTrue(is_sorted([2, 4]))
        self.assertTrue(is_sorted([5, 9]))
        self.assertTrue(is_sorted([]))

    def test_sortArrayByParity(self):
        solution = Solution()
        self.assertTrue(is_sorted(solution.sortArrayByParity([1, 6, 3, 4, 5])))
        self.assertTrue(is_sorted(solution.sortArrayByParity([9, 7, 5, 3, 2, 4, 6, 8])))
        self.assertTrue(is_sorted(solution.sortArrayByParity([1, 3])))
        self.assertTrue(is_sorted(solution.sortArrayByParity([2, 4])))
        self.assertTrue(is_sorted(solution.sortArrayByParity([1])))
        self.assertTrue(is_sorted(solution.sortArrayByParity([])))


if __name__ == '__main__':
    unittest.main()

