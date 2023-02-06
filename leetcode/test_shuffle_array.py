# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].


import unittest


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        shuffled = []
        for i in range(0, int(n)):
            shuffled.append(nums[i])
            shuffled.append(nums[i + n])
        return shuffled


class TestShuffleArr(unittest.TestCase):
    def test_shuffle(self):
        solution = Solution()
        self.assertEqual(solution.shuffle([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7])
        self.assertEqual(solution.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4), [1, 4, 2, 3, 3, 2, 4, 1])
        self.assertEqual(solution.shuffle([1, 1, 2, 2], 2), [1, 2, 1, 2])
        self.assertEqual(solution.shuffle([1, 2], 1), [1, 2])


if __name__ == '__main__':
    unittest.main()
