# Given an integer n, return true if it is a power of two.
# Otherwise, return false.


import unittest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1


class TestSolution(unittest.TestCase):
    def test_isPowerOfTwo(self):
        solution = Solution()
        self.assertTrue(solution.isPowerOfTwo(8))
        self.assertTrue(solution.isPowerOfTwo(256))
        self.assertTrue(solution.isPowerOfTwo(1024))
        self.assertFalse(solution.isPowerOfTwo(22))
        self.assertFalse(solution.isPowerOfTwo(0))
        self.assertFalse(solution.isPowerOfTwo(1000))
        self.assertFalse(solution.isPowerOfTwo(-16))
