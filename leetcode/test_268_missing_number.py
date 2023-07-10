# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.


import unittest


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        maximum = len(nums)
        sum_perfect = maximum * (maximum + 1) / 2
        sum_real = sum(nums)
        result = int(sum_perfect - sum_real)
        return result


class TestMissingNum(unittest.TestCase):
    def test_missingNumber(self):
        solution = Solution()
        self.assertEqual(2, solution.missingNumber([0, 1]))
        self.assertEqual(2, solution.missingNumber([3, 0, 1]))
        self.assertEqual(8, solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


if __name__ == '__main__':
    unittest.main()
