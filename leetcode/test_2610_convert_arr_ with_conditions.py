# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
#
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.


import unittest


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result = [set()]
        for num in nums:
            added = False
            for sub in result:
                if num not in sub:
                    sub.add(num)
                    added = True
                    break
            if not added:
                result.append({num})
        result = [list(r) for r in result]
        return result


class TestSolution(unittest.TestCase):
    def test_findMatrix(self):
        solution = Solution()
        self.assertEqual([[1, 2, 3, 4], [1, 3], [1]], solution.findMatrix([1, 3, 4, 1, 2, 3, 1]))
        self.assertEqual([[1, 2, 3, 4]], solution.findMatrix([1, 2, 3, 4]))
