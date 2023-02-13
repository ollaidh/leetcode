# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it.

import unittest


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                curr = pascal[i-1][j-1] + pascal[i-1][j]
                row.append(curr)
            row.append(1)
            pascal.append(row)

        return pascal


class TestGenerate(unittest.TestCase):
    def test_generate(self):
        solution = Solution()
        self.assertEqual(solution.generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
        self.assertEqual(solution.generate(1), [[1]])


if __name__ == '__main__':
    unittest.main()
