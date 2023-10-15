# We are given a list nums of integers representing a list
# compressed with run-length encoding.
#
# Consider each adjacent pair of elements [freq, val] = [nums[2*i],
# nums[2*i+1]] (with i >= 0).  For each such pair, there are freq
# elements with value val concatenated in a sublist. Concatenate
# all the sublists from left to right to generate the decompressed list.
#
# Return the decompressed list.


import unittest


class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []
        i = 1
        while i < len(nums):
            result.extend([nums[i]] * nums[i - 1])
            i += 2
        return result


class TestSolution(unittest.TestCase):
    def test_decompressRLElist(self):
        solution = Solution()
        self.assertEqual([2, 4, 4, 4], solution.decompressRLElist([1, 2, 3, 4]))
        self.assertEqual([1, 3, 3], solution.decompressRLElist([1, 1, 2, 3]))
        self.assertEqual([1, 2, 3], solution.decompressRLElist([1, 1, 1, 2, 1, 3]))
