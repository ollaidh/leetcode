# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.


import unittest


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []

        freq = set()
        for num in nums:
            freq.add(num)

        for i in range(1, len(nums) + 1):
            if i not in freq:
                result.append(i)

        return result


class TestFindDisapp(unittest.TestCase):
    def test_findDisappearedNumbers(self):
        solution = Solution()
        self.assertEqual([5, 6], solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
        self.assertEqual([2], solution.findDisappearedNumbers([1, 1]))


if __name__ == '__main__':
    unittest.main()
