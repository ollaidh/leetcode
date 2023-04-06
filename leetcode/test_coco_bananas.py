# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours. Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.


import unittest
import math


class Solution:
    def get_eating_time(self, piles: list[int], velocity: int):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / velocity)
        return hours

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_bananas = max(piles)
        lp, rp = 1, min_bananas
        while lp <= rp:
            velocity = lp + (rp - lp) // 2
            hours = self.get_eating_time(piles, velocity)
            if hours <= h:
                rp = velocity - 1
                min_bananas = min(min_bananas, velocity)
            else:
                lp = velocity + 1
        return min_bananas


class TestEatingSpeed(unittest.TestCase):
    def test_get_eating_time(self):
        solution = Solution()
        self.assertEqual(solution.get_eating_time([1, 2, 5], 2), 5)
        self.assertEqual(solution.get_eating_time([10], 3), 4)

    def test_minEatingSpeed(self):
        solution = Solution()
        self.assertEqual(solution.minEatingSpeed([3, 6, 7, 11], 8), 4)
        self.assertEqual(solution.minEatingSpeed([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(solution.minEatingSpeed([30, 11, 23, 4, 20], 6), 23)
        self.assertEqual(solution.minEatingSpeed([312884470], 312884469), 2)
        self.assertEqual(solution.minEatingSpeed(
            [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589,
             290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184],
            823855818), 14)


if __name__ == '__main__':
    unittest.main()
