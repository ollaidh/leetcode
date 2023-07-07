# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle


import unittest


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [0] * (rowIndex + 1)
        result[0] = 1
        result[1] = 1
        for i in range(2, rowIndex + 1):
            backup = 1
            for j in range(1, i):
                stash = result[j]
                result[j] += backup
                backup = stash
            result[i] = 1
        return result


class TestGR(unittest.TestCase):
    def test_getRow(self):
        solution = Solution()
        self.assertEqual([1, 3, 3, 1], solution.getRow(3))
        self.assertEqual([1], solution.getRow(0))
        self.assertEqual([1, 1], solution.getRow(1))


if __name__ == '__main__':
    unittest.main()
