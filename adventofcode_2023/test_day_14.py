import unittest
import pathlib


class Board:
    def __init__(self, disposition: list[list[str]]):
        self.disposition = disposition
        self.weight = 0

    def __eq__(self, other):
        return self.disposition == other.disposition

    def __str__(self):
        printed = ""
        for line in self.disposition:
            printed += str(line)
            printed += "\n"
        return printed

    def roll_stone_north(self, start_line: int, start_column: int):
        if start_line == 0:
            return

        stop_line = start_line
        while stop_line > 0:
            if self.disposition[stop_line - 1][start_column] in ["#", "O"]:
                self.disposition[start_line][start_column] = "."
                self.disposition[stop_line][start_column] = "O"
                return
            stop_line -= 1
        self.disposition[stop_line][start_column] = "O"
        self.disposition[start_line][start_column] = "."

    def roll_stone_south(self, start_line: int, start_column: int):
        if start_line == len(self.disposition) - 1:
            return

        stop_line = start_line
        while stop_line < len(self.disposition) - 1:
            if self.disposition[stop_line + 1][start_column] in ["#", "O"]:
                self.disposition[start_line][start_column] = "."
                self.disposition[stop_line][start_column] = "O"
                return
            stop_line += 1
        self.disposition[stop_line][start_column] = "O"
        self.disposition[start_line][start_column] = "."

    def roll_board(self):
        for j in range(len(self.disposition[0])):
            for i in range(len(self.disposition)):
                if self.disposition[i][j] == "O":
                    self.roll_stone_north(i, j)

    def calc_weight(self):
        for j in range(len(self.disposition[0])):
            for i in range(len(self.disposition)):
                if self.disposition[i][j] == "O":
                    curr_weight = len(self.disposition) - i
                    self.weight += curr_weight


def get_board_from_file(filepath: str) -> list[list[str]]:
    filepath_inp = pathlib.Path(__file__).parent.resolve() / filepath
    with open(filepath_inp) as f:
        board = []
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            if line:
                board.append([symbol for symbol in line])

        return board


class TestRollStones(unittest.TestCase):
    def test_roll_stone_north(self):
        board1 = Board([
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["O"],
            ["."],
        ])
        expected_result1 = Board([
            ["O"],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
        ])
        board1.roll_stone_north(5, 0)
        self.assertEqual(expected_result1, board1)

        board2 = Board([
            ["O"],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
        ])
        expected_result2 = Board([
            ["O"],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
        ])
        board2.roll_stone_north(0, 0)
        self.assertEqual(expected_result2, board2)

        board3 = Board([
            ["."],
            ["O"],
            ["."],
            ["."],
            ["O"],
            ["."],
            ["."],
        ])
        expected_result3 = Board([
            ["."],
            ["O"],
            ["O"],
            ["."],
            ["."],
            ["."],
            ["."],
        ])
        board3.roll_stone_north(4, 0)
        self.assertEqual(expected_result3, board3)

    def test_roll_stone_south(self):
        board1 = Board([
            ["."],
            ["O"],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
        ])
        expected_result1 = Board([
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["O"],
        ])
        board1.roll_stone_south(1, 0)
        self.assertEqual(expected_result1, board1)

        board2 = Board([
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["O"],
        ])
        expected_result2 = Board([
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["."],
            ["O"],
        ])
        board2.roll_stone_south(6, 0)
        self.assertEqual(expected_result2, board2)

        board3 = Board([
            ["O"],
            ["."],
            ["."],
            ["."],
            ["."],
            ["O"],
            ["."],
        ])
        expected_result3 = Board([
            ["."],
            ["."],
            ["."],
            ["."],
            ["O"],
            ["O"],
            ["."],
        ])
        board3.roll_stone_south(0, 0)
        print(board3)
        self.assertEqual(expected_result3, board3)

    def test_roll_board_north(self):
        board = Board([
            ['O', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
            ['O', '.', 'O', 'O', '#', '.', '.', '.', '.', '#'],
            ['.', '.', '.', '.', '.', '#', '#', '.', '.', '.'],
            ['O', 'O', '.', '#', 'O', '.', '.', '.', '.', 'O'],
            ['.', 'O', '.', '.', '.', '.', '.', 'O', '#', '.'],
            ['O', '.', '#', '.', '.', 'O', '.', '#', '.', '#'],
            ['.', '.', 'O', '.', '.', '#', 'O', '.', '.', 'O'],
            ['.', '.', '.', '.', '.', '.', '.', 'O', '.', '.'],
            ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.'],
            ['#', 'O', 'O', '.', '.', '#', '.', '.', '.', '.']
        ])
        expected_result = Board([
            ['O', 'O', 'O', 'O', '.', '#', '.', 'O', '.', '.'],
            ['O', 'O', '.', '.', '#', '.', '.', '.', '.', '#'],
            ['O', 'O', '.', '.', 'O', '#', '#', '.', '.', 'O'],
            ['O', '.', '.', '#', '.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
            ['.', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
            ['.', '.', 'O', '.', '.', '#', '.', 'O', '.', 'O'],
            ['.', '.', 'O', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.'],
            ['#', '.', '.', '.', '.', '#', '.', '.', '.', '.']
        ])
        board.roll_board()
        self.assertEqual(expected_result, board)


if __name__ == '__main__':
    # board_data = get_board_from_file('inputs/input_day_14.dat')
    # board = Board(board_data)
    # board.roll_board()
    # board.calc_weight()
    # print(board.weight)
    unittest.main()
