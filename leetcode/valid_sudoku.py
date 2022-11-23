# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.


import unittest


class Solution:
    def isValidSudoku(self, board):
        lines = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue

                if value in lines[i]:
                    return False
                if value in columns[j]:
                    return False
                if value in squares[i // 3][j // 3]:
                    return False

                lines[i].add(value)
                columns[j].add(value)
                squares[i // 3][j // 3].add(value)

        return True


class TestValidSudoku(unittest.TestCase):
    def test_create(self):
        solution = Solution()
        matrix1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        matrix2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        matrix3 = [['.'] * 9] * 9
        self.assertEqual(solution.isValidSudoku(matrix1), True)
        self.assertEqual(solution.isValidSudoku(matrix2), False)
        self.assertEqual(solution.isValidSudoku(matrix3), True)


if __name__ == '__main__':
    unittest.main()
