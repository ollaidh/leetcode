# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and
# numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers,index1 and index2, added by one as an integer array [index1,index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.


import unittest


class Solution:
    def initial_right_pointer(self, numbers: list[int], num: int) -> int:
        lp = 0
        rp = len(numbers) - 1
        while lp + 1 < rp:
            mid = lp + (rp - lp) // 2
            if numbers[mid] <= num:
                lp = mid
            else:
                rp = mid
        return lp + 1

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lp = 0
        rp = self.initial_right_pointer(numbers, target - numbers[0])
        while numbers[lp] + numbers[rp] != target:
            if numbers[lp] + numbers[rp] < target:
                lp += 1
            else:
                rp -= 1
        return [lp + 1, rp + 1]


class TestTwoSum(unittest.TestCase):
    def test_initial_left_pointer(self):
        solution = Solution()
        self.assertEqual(solution.initial_right_pointer([1, 2, 3, 7, 11, 15], 9), 4)
        self.assertEqual(solution.initial_right_pointer([2, 6, 11, 15], 6), 2)
        self.assertEqual(solution.initial_right_pointer([2, 3, 4], 6), 2)
        self.assertEqual(solution.initial_right_pointer([-1, 0], -1), 1)

    def test_twoSum(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(solution.twoSum([2, 3, 4], 6), [1, 3])
        self.assertEqual(solution.twoSum([-1, 0], -1), [1, 2])


if __name__ == '__main__':
    unittest.main()
