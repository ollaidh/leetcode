# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive.


import unittest


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewels = set(jewels)
        for s in stones:
            if s in jewels:
                result += 1

        return result


class TestSolution(unittest.TestCase):
    def test_numJewelsInStones(self):
        solution = Solution()
        self.assertEqual(3, solution.numJewelsInStones("aA", "aAAbbbb"))
        self.assertEqual(0, solution.numJewelsInStones("s", "SSSSS"))