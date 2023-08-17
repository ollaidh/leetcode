# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.


import unittest


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        smaller = {num: None for num in nums}
        srt = sorted(nums)
        for i, num in enumerate(srt):
            if num in smaller and smaller[num] is None:
                smaller[num] = i

        result = [smaller[val] for val in nums]

        return result


class TestSNThC(unittest.TestCase):
    def test_smallerNumbersThanCurrent(self):
        solution = Solution()
        self.assertEqual([4, 0, 1, 1, 3], solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
        self.assertEqual([2, 1, 0, 3], solution.smallerNumbersThanCurrent([6, 5, 4, 8]))
        self.assertEqual([0, 0, 0, 0], solution.smallerNumbersThanCurrent([7, 7, 7, 7]))


if __name__ == "__main__":
    unittest.main()
