# There are numBottles water bottles that are initially full of water.
# You can exchange numExchange empty water bottles from the market with one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.


import unittest


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty_bottles = 0
        drunk_bottles = full_bottles
        while full_bottles > 0 or empty_bottles >= numExchange:
            empty_bottles += full_bottles
            full_bottles = empty_bottles // numExchange
            drunk_bottles += full_bottles
            empty_bottles -= numExchange * full_bottles
        return drunk_bottles


class TestWaterBottles(unittest.TestCase):
    def test_waterbottles(self):
        solution = Solution()
        self.assertEqual(solution.numWaterBottles(9, 3), 13)
        self.assertEqual(solution.numWaterBottles(15, 4), 19)


if __name__ == '__main__':
    unittest.main()