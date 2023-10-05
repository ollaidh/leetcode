# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the
# maximum average value and return this value. Any answer with a calculation error
# less than 10-5 will be accepted.


import unittest


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        result = sum(nums[:k]) / k
        curr_avg = result
        i = 0
        while i + k < len(nums):
            curr_avg = curr_avg + (nums[i + k] - nums[i]) / k
            result = max(result, curr_avg)
            i += 1
        return result


class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()
        self.assertEqual(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75000)
        self.assertEqual(solution.findMaxAverage([5], 1), 5.00000)


if __name__ == '__mein__':
    unittest.main()
