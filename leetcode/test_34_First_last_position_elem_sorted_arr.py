# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
# of a given target value. If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.


import unittest


def find_mid_elem(seq: list[int], value: int) -> int:
    lp = 0
    rp = len(seq) - 1

    while lp <= rp:
        mid = lp + (rp - lp) // 2
        if seq[mid] < value:
            lp = mid + 1
        elif seq[mid] > value:
            rp = mid - 1
        else:
            return mid
    return - 1


def find_left_elem(seq: list[int], value: int) -> int:
    lp = 0
    rp = len(seq) - 1

    if seq[lp] == value:
        return 0

    while lp <= rp:
        mid = lp + (rp - lp) // 2
        if seq[mid] < value:
            if seq[mid + 1] < value:
                lp = mid + 1
            else:
                return mid + 1
        else:
            if seq[mid] == value:
                if seq[mid - 1] == value:
                    rp = mid - 1
                else:
                    return mid
    return - 1


def find_right_elem(seq: list[int], value: int) -> int:
    lp = 0
    rp = len(seq) - 1

    if seq[rp] == value:
        return rp

    while lp <= rp:
        mid = lp + (rp - lp) // 2
        if seq[mid] == value:
            if seq[mid + 1] == value:
                lp = mid + 1
            else:
                return mid
        else:
            if seq[mid - 1] > value:
                rp = mid - 1
            else:
                return mid - 1
    return - 1


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        pos_curr = find_mid_elem(nums, target)
        if pos_curr == -1:
            return [-1, -1]
        lp = find_left_elem(nums[:pos_curr + 1], target)
        rp = pos_curr + find_right_elem(nums[pos_curr:], target)
        return [lp, rp]


class TestSolution(unittest.TestCase):
    def test_find_elem_mid(self):
        self.assertEqual(1, find_mid_elem([5, 6, 7, 8, 9, 10, 11], 6))
        self.assertEqual(1, find_mid_elem([5, 6, 7, 8, 9, 10, 11, 12], 6))
        self.assertEqual(5, find_mid_elem([5, 6, 7, 8, 9, 10, 11], 10))
        self.assertEqual(0, find_mid_elem([5, 6, 7, 8, 9, 10, 11], 5))
        self.assertEqual(6, find_mid_elem([5, 6, 7, 8, 9, 10, 11], 11))
        self.assertEqual(-1, find_mid_elem([5, 6, 7, 9, 10, 11], 8))
        self.assertEqual(0, find_mid_elem([11], 11))

    def test_find_elem_left(self):
        self.assertEqual(3, find_left_elem([5, 6, 7, 8, 8, 8, 8], 8))
        self.assertEqual(5, find_left_elem([5, 6, 7, 9, 10, 11, 11], 11))
        self.assertEqual(6, find_left_elem([5, 6, 7, 9, 10, 11, 12], 12))
        self.assertEqual(0, find_left_elem([2, 2, 2], 2))
        self.assertEqual(0, find_left_elem([2, 2], 2))
        self.assertEqual(3, find_left_elem([0, 0, 1, 2, 2], 2))

    def test_find_elem_right(self):
        self.assertEqual(2, find_right_elem([1, 1, 1, 2, 3, 4], 1))
        self.assertEqual(1, find_right_elem([1, 1, 2, 3, 4], 1))
        self.assertEqual(0, find_right_elem([1, 2, 3, 4], 1))
        self.assertEqual(2, find_right_elem([2, 2, 2], 2))
        self.assertEqual(1, find_right_elem([2, 2], 2))

    def test_searchRange(self):
        solution = Solution()
        self.assertEqual([3, 4], solution.searchRange([5, 7, 7, 8, 8, 10], 8))
        self.assertEqual([-1, -1], solution.searchRange([5, 7, 7, 8, 8, 10], 6))
        self.assertEqual([3, 3], solution.searchRange([5, 7, 7, 8, 9, 9], 8))
        self.assertEqual([-1, -1], solution.searchRange([], 0))
        self.assertEqual([0, 0], solution.searchRange([1], 1))
        self.assertEqual([-1, -1], solution.searchRange([2, 2], 3))
        self.assertEqual([0, 2], solution.searchRange([2, 2, 2], 2))
        self.assertEqual([2, 5], solution.searchRange([1, 2, 3, 3, 3, 3, 4, 5, 9], 3))
        self.assertEqual([3, 4], solution.searchRange([0, 0, 1, 2, 2], 2))
