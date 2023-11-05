# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
# to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


import unittest


def validate_rows(board: list[list[str]]) -> bool:
    for row in board:
        nums = set()
        for num in row:
            if num == ".":
                continue
            if num not in nums:
                nums.add(num)
            else:
                return False
    return True


def validate_columns(board: list[list[str]]) -> bool:
    field_size = len(board)
    for j in range(field_size):
        nums = set()
        for i in range(field_size):
            if board[i][j] == ".":
                continue
            if board[i][j] not in nums:
                nums.add(board[i][j])
            else:
                return False
    return True


def board_to_squares_coord(board_i: int, board_j: int) -> tuple:
    return board_i // 3, board_j // 3


def validate_squares(board: list[list[str]]) -> bool:
    field_size = len(board)
    squares = [[set() for _ in range(len(board))] for _ in range(len(board))]
    for i in range(field_size):
        for j in range(field_size):
            if board[i][j] == ".":
                continue
            sq_i, sq_j = board_to_squares_coord(i, j)
            if board[i][j] not in squares[sq_i][sq_j]:
                squares[sq_i][sq_j].add(board[i][j])
            else:
                return False
    return True


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        funcs = [validate_rows, validate_columns, validate_squares]
        # funcs = [validate_rows, validate_columns]

        for func in funcs:
            if not func(board):
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_board_to_squares_coord(self):
        self.assertEqual((0, 0), board_to_squares_coord(1, 2))
        self.assertEqual((1, 1), board_to_squares_coord(5, 5))
        self.assertEqual((0, 1), board_to_squares_coord(2, 4))
        self.assertEqual((2, 2), board_to_squares_coord(8, 8))

    def test_validations(self):
        self.assertTrue(validate_rows([["1", "2", "3"], ["1", ".", "3"], ["1", "2", "3"]]))
        self.assertTrue(validate_columns([["1", ".", "1"], ["2", "2", "2"], ["3", "3", "3"]]))
        self.assertTrue(validate_squares([["1", "2", "3"], ["4", ".", "5"], [".", ".", "."]]))

    def test_isValidSudoku(self):
        solution = Solution()
        self.assertTrue(solution.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                                [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
        self.assertFalse(solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                                                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
        self.assertFalse(solution.isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."],
                                                 [".", "4", ".", "3", ".", ".", ".", ".", "."],
                                                 [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                                                 ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                                                 [".", ".", "2", ".", "7", ".", ".", ".", "."],
                                                 [".", "1", "5", ".", ".", ".", ".", ".", "."],
                                                 [".", ".", ".", ".", ".", "2", ".", ".", "."],
                                                 [".", "2", ".", "9", ".", ".", ".", ".", "."],
                                                 [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
