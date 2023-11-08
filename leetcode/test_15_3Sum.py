# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


import unittest


def twoSumSorted(target: int, sequence: list[int]) -> list[list[int]] | None:
    lp = 0
    rp = len(sequence) - 1
    result = []
    firsts = set()

    while lp < rp:
        if sequence[lp] + sequence[rp] < target:
            lp += 1
        elif sequence[lp] + sequence[rp] > target:
            rp -= 1
        else:
            if sequence[lp] not in firsts:
                result.append([-target, sequence[lp], sequence[rp]])
                firsts.add(sequence[lp])
            lp += 1
            rp -= 1
    return result


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            curr_pairs = twoSumSorted(- nums[i], nums[i + 1:])
            result.extend(curr_pairs)
        return result


class TestSolution(unittest.TestCase):
    def test_twoSumSorted(self):
        seq = [1, 2, 3, 4, 5, 6]
        target = 4
        self.assertEqual([[-4, 1, 3]], twoSumSorted(target, seq))

        seq = [0, 0, 0, 0]
        target = 0
        self.assertEqual([[0, 0, 0]], twoSumSorted(target, seq))

    def test_threeSum(self):
        solution = Solution()
        self.assertEqual([[0, 0, 0]], solution.threeSum([0, 0, 0, 0]))
        self.assertEqual([[-2, 0, 2]], solution.threeSum([-2, 0, 0, 2, 2]))
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], solution.threeSum([-1, 0, 1, 2, -1, -4]))
        self.assertEqual([], solution.threeSum([0, 1, 1]))
        self.assertEqual([[0, 0, 0]], solution.threeSum([0, 0, 0]))
