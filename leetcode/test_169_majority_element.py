# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# Majority element always exists in the array.
# Solve linear time and in O(1) space


import unittest


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = 0
        result = nums[0]
        for num in nums:
            if counter == 0:
                result = num
            if num == result:
                counter += 1
            else:
                counter -= 1
        return result


class TestME(unittest.TestCase):
    def test_majorityElement(self):
        solution = Solution()

        self.assertEqual(3, solution.majorityElement([3, 2, 3]))
        self.assertEqual(2, solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
        self.assertEqual(3, solution.majorityElement([3, 3, 3, 3]))
        self.assertEqual(5, solution.majorityElement([5]))


if __name__ == '__main__':
    unittest.main()
