# Given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith
# line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container,
# such that the container contains the most water. Return the maximum amount of water a container can store.


import unittest


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_volume = min(height[left], height[right]) * (len(height) - 1)

        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            test_volume = min(height[left], height[right]) * (right - left)
            if test_volume >= max_volume:
                max_volume = test_volume

        return max_volume


class TestMaxArea(unittest.TestCase):
    def test_maxArea(self):
        solution = Solution()
        self.assertEqual(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(solution.maxArea([1, 1]), 1)
        self.assertEqual(solution.maxArea([4, 3, 2, 1, 4]), 16)
        self.assertEqual(solution.maxArea([2, 3, 4, 5, 18, 17, 6]), 17)


if __name__ == '__main__':
    unittest.main()
