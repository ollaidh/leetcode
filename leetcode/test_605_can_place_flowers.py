# You have a long flowerbed in which some of the plots are planted,
# and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without
# violating the no-adjacent-flowers rule and false otherwise.


import unittest


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        counter = 1
        for plot in flowerbed:
            if plot == 0:
                counter += 1
                if counter == 3:
                    n -= 1
                    counter = 1
            else:
                counter = 0
            if n == 0:
                return True
        return n == 1 and counter == 2


class TestSolution(unittest.TestCase):
    def test_canPlaceFlowers(self):
        solution = Solution()
        self.assertTrue(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertFalse(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))
        self.assertFalse(solution.canPlaceFlowers([0, 0, 0, 0, 1], 3))
        self.assertTrue(solution.canPlaceFlowers([0], 1))
        self.assertTrue(solution.canPlaceFlowers([0, 0], 1))
        self.assertTrue(solution.canPlaceFlowers([1, 0, 0, 0, 1], 0))


if __name__ == '__mein__':
    unittest.main()
