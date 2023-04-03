# You are given an m x n integer matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.


import unittest


class Solution:
    def convert_to_ij(self, index: int, row_length: int) -> tuple:
        i = index // row_length
        j = index % row_length
        return i, j

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0])
        while left + 1 < right:
            middle_i, middle_j = self.convert_to_ij(left + (right - left) // 2, len(matrix[0]))

            if matrix[middle_i][middle_j] == target:
                return True
            elif matrix[middle_i][middle_j] > target:
                right = left + (right - left) // 2
            else:
                left = left + (right - left) // 2
        return matrix[0][0] == target


class TestSearchMatrix(unittest.TestCase):
    def test_convert_to_ij(self):
        solution = Solution()
        self.assertEqual(solution.convert_to_ij(5, 4), (1, 1))
        self.assertEqual(solution.convert_to_ij(9, 4), (2, 1))
        self.assertEqual(solution.convert_to_ij(0, 1), (0, 0))

    def test_searchMatrix(self):
        solution = Solution()
        self.assertTrue(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
        self.assertFalse(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
        self.assertTrue(solution.searchMatrix([[1]], 1))


if __name__ == '__main__':
    unittest.main()
