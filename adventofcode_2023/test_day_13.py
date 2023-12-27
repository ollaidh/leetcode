import unittest
import pathlib


def rotate_matrix(field: list[list[str]]) -> list[list[str]]:
    rows, cols = len(field), len(field[0])
    rotated_field = [[''] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            rotated_field[j][rows - 1 - i] = field[i][j]
    return rotated_field


def find_symetry(matrix: list[list[str]]) -> tuple[int, str]:
    symmetry_types = {'hor': matrix, 'vert': rotate_matrix(matrix)}
    for symmetry_type in symmetry_types:
        field = symmetry_types[symmetry_type]
        for i in range(len(field) - 1):
            symmetry = True
            if field[i] == field[i + 1]:
                up_index = i - 1
                down_index = i + 2
                while up_index >= 0 and down_index <= len(field) - 1:
                    if field[up_index] != field[down_index]:
                        symmetry = False
                        break
                    up_index -= 1
                    down_index += 1
                if symmetry:
                    return i + 1, symmetry_type
    assert False


def count_smudges_in_rows(row1: list[str], row2: list[str]) -> int:
    result = 0
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            result += 1
    return result


def count_smudges(matrix: list[list[str]], row_index: int) -> int:
    result = 0
    top_row = row_index
    bot_row = top_row + 1
    while top_row >= 0 and bot_row < len(matrix):
        result += count_smudges_in_rows(matrix[top_row], matrix[bot_row])
        top_row -= 1
        bot_row += 1
    return result


def find_smudged_symetry(matrix: list[list[str]]) -> tuple[int, str]:
    symmetry_types = {'hor': matrix, 'vert': rotate_matrix(matrix)}
    for symmetry_type in symmetry_types:
        field = symmetry_types[symmetry_type]
        for i in range(len(field) - 1):
            symmetry = count_smudges(field, i)
            if symmetry == 1:
                return i + 1, symmetry_type
    assert False


def play(input_path: str, symmetry_type: str) -> int:
    symmetry_types = {'straight': find_symetry, 'smudged': find_smudged_symetry}
    filepath_inp = pathlib.Path(__file__).parent.resolve() / input_path
    result = 0
    with open(filepath_inp) as f:
        block = []
        lines = f.readlines()
        last_line_id, line_id = len(lines) - 1, 0
        for line in lines:
            line = line.rstrip()
            if line:
                block.append([symbol for symbol in line])
            if line_id == last_line_id or not line:
                curr_result, type_sym = symmetry_types[symmetry_type](block)
                if type_sym == 'hor':
                    result += 100 * curr_result
                else:
                    result += curr_result
                block = []
            line_id += 1
    return result


class TestIncidence(unittest.TestCase):
    def test_rotate_matrix(self):
        matrix = [
            ['.', '#', '.', '#'],
            ['#', '.', '#', '.'],
            ['.', '#', '.', '#']
        ]
        expected = [
            ['.', '#', '.'],
            ['#', '.', '#'],
            ['.', '#', '.'],
            ['#', '.', '#']
        ]
        self.assertEqual(expected, rotate_matrix(matrix))

        matrix = [
            ['.', '#', '.', '#', '.', '#'],
            ['#', '.', '#', '.', '#', '.'],
            ['.', '#', '.', '#', '.', '#'],
            ['#', '.', '#', '.', '#', '.'],
            ['.', '#', '.', '#', '.', '#']
        ]
        expected = [
            ['.', '#', '.', '#', '.'],
            ['#', '.', '#', '.', '#'],
            ['.', '#', '.', '#', '.'],
            ['#', '.', '#', '.', '#'],
            ['.', '#', '.', '#', '.'],
            ['#', '.', '#', '.', '#']
        ]
        self.assertEqual(expected, rotate_matrix(matrix))

    def test_find_symetry(self):
        field = [
            ['#', '.', '.', '.', '#', '#', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '#', '.', '.', '#'],
            ['.', '.', '#', '#', '.', '.', '#', '#', '#'],
            ['#', '#', '#', '#', '#', '.', '#', '#', '.'],
            ['#', '#', '#', '#', '#', '.', '#', '#', '.'],
            ['.', '.', '#', '#', '.', '.', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '#', '.', '.', '#']
        ]
        self.assertEqual((4, 'hor'), find_symetry(field))

        field = [
            ['#', '.', '#', '#', '.', '.', '#', '#', '.'],
            ['.', '.', '#', '.', '#', '#', '.', '#', '.'],
            ['#', '#', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '#', '.', '#', '#', '.', '#', '.'],
            ['.', '.', '#', '#', '.', '.', '#', '#', '.'],
            ['#', '.', '#', '.', '#', '#', '.', '#', '.']
        ]
        self.assertEqual((5, 'vert'), find_symetry(field))

    def test_find_smudged_symetry(self):
        field = [
            ['#', '.', '.', '.', '#', '#', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '#', '.', '.', '#'],
            ['.', '.', '#', '#', '.', '.', '#', '#', '#'],
            ['#', '#', '#', '#', '#', '.', '#', '#', '.'],
            ['#', '#', '#', '#', '#', '.', '#', '#', '.'],
            ['.', '.', '#', '#', '.', '.', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '#', '.', '.', '#']
        ]
        self.assertEqual((1, 'hor'), find_smudged_symetry(field))

        field = [
            ['#', '.', '#', '#', '.', '.', '#', '#', '.'],
            ['.', '.', '#', '.', '#', '#', '.', '#', '.'],
            ['#', '#', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '.', '.', '.', '.', '.', '.', '#'],
            ['.', '.', '#', '.', '#', '#', '.', '#', '.'],
            ['.', '.', '#', '#', '.', '.', '#', '#', '.'],
            ['#', '.', '#', '.', '#', '#', '.', '#', '.']
        ]
        self.assertEqual((3, 'hor'), find_smudged_symetry(field))

        field = [
            ['#', '.', '#', '#', '.', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '.'],
            ['.', '#', '.', '.', '#', '.', '.'],
            ['#', '.', '#', '#', '.', '#', '#'],
            ['.', '#', '.', '.', '#', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '#'],
            ['.', '#', '.', '.', '#', '.', '#'],
            ['.', '#', '.', '.', '#', '.', '#'],
            ['#', '.', '.', '.', '.', '#', '.'],
            ['#', '.', '.', '.', '.', '#', '#'],
            ['#', '.', '.', '.', '.', '#', '#'],
            ['#', '.', '.', '.', '.', '#', '.'],
            ['.', '#', '.', '.', '#', '.', '#'],
            ['.', '#', '.', '.', '#', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '#'],
            ['.', '#', '.', '.', '#', '.', '#'],
            ['#', '.', '#', '#', '.', '#', '.']
        ]
        self.assertEqual((10, 'hor'), find_smudged_symetry(field))

        field = [
            ['.', '#', '#', '.', '#', '.', '.', '#', '.', '#', '#', '.', '#', '#', '#'],
            ['#', '#', '#', '#', '.', '#', '.', '.', '#', '#', '#', '#', '#', '#', '#'],
            ['.', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '#', '.', '#', '#'],
            ['.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '.', '.'],
            ['.', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#', '.', '.'],
            ['.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '#', '#', '#']
        ]
        self.assertEqual((2, 'vert'), find_smudged_symetry(field))

    def test_play(self):
        result = play('inputs_tests/input_day_13_test.dat', 'straight')
        self.assertEqual(405, result)

        result = play('inputs_tests/input_day_13_test.dat', 'smudged')
        self.assertEqual(400, result)


if __name__ == '__main__':
    print(play('inputs/input_day_13.dat', 'straight'))
    print(play('inputs/input_day_13.dat', 'smudged'))
