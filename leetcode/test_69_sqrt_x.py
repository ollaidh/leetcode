# Given a non-negative integer x, return the square root of x
# rounded down to the nearest integer. The returned integer should be non-negative as well.
# Not use any built-in exponent function or operator.


import unittest


class Solution:
    def mySqrt(self, x: int) -> int:
        lp, rp = 0, x
        while lp <= rp:
            mid = (lp + rp) // 2
            pow_2 = mid * mid
            if pow_2 == x:
                return mid
            if pow_2 > x:
                rp = mid - 1
            else:
                lp = mid + 1

        return rp


class TestSqrt(unittest.TestCase):
    def test_mySqrt(self):
        solution = Solution()
        self.assertEqual(2, solution.mySqrt(5))
        self.assertEqual(2, solution.mySqrt(4))
        self.assertEqual(2, solution.mySqrt(8))
        self.assertEqual(6, solution.mySqrt(36))


if __name__ == '__main__':
    unittest.main()
