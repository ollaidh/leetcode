# You are given a 0-indexed, strictly increasing integer array nums
# and a positive integer diff. A triplet (i, j, k) is an arithmetic
# triplet if the following conditions are met:
# - i < j < k,
# - nums[j] - nums[i] == diff, and
# - nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.


import unittest


class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        result = 0
        diffs = {num: num + diff for num in nums}
        for num in nums:
            if num + diff in diffs:
                if diffs[num + diff] in diffs:
                    result += 1

        return result


class TestSolution(unittest.TestCase):
    def test_arithmeticTriplets(self):
        solution = Solution()
        self.assertEqual(2, solution.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))
        self.assertEqual(2, solution.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))
