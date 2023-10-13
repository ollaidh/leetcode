# You are given an integer array nums with the following properties:
# - nums.length == 2 * n.
# - nums contains n + 1 unique elements.
# - Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.


import unittest


class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        unique = set()
        for num in nums:
            if num in unique:
                return num
            unique.add(num)


class TestSolition(unittest.TestCase):
    def test_repeatedNTimes(self):
        solution = Solution()
        self.assertEqual(3, solution.repeatedNTimes([1, 2, 3, 3]))
        self.assertEqual(4, solution.repeatedNTimes([4, 4, 1, 2, 3]))
        self.assertEqual(5, solution.repeatedNTimes([1, 2, 3, 5, 5]))
        self.assertEqual(4, solution.repeatedNTimes([7, 8, 9, 4, 4, 10]))
        self.assertEqual(-2, solution.repeatedNTimes([-2, -2, -3, -1, 0]))
        self.assertEqual(8, solution.repeatedNTimes([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]))
        self.assertEqual(42, solution.repeatedNTimes([42, 42, 42, 42]))
        self.assertEqual(0, solution.repeatedNTimes([0, 0]))
