import unittest
import pathlib
from typing import Tuple


class PipeField:
    def __init__(self, field: list[list[str]]):
        self.field = field
        for i in range(len(self.field)):
            for j in range(len(self.field)):
                if self.field[i][j] == 'S':
                    self.start_x = i
                    self.start_y = j
                    break

    def get_directions(self, x_pos: int, y_pos) -> tuple[tuple[int, int], tuple[int, int]]:
        pipe = self.field[x_pos][y_pos]
        if pipe == '|':
            return (x_pos - 1, y_pos), (x_pos + 1, y_pos)
        if pipe == '-':
            return (x_pos, y_pos - 1), (x_pos, y_pos + 1)
        if pipe == 'L':
            return (x_pos - 1, y_pos), (x_pos, y_pos + 1)
        if pipe == 'J':
            return (x_pos - 1, y_pos), (x_pos, y_pos - 1)
        if pipe == '7':
            return (x_pos + 1, y_pos), (x_pos, y_pos - 1)
        if pipe == 'F':
            return (x_pos + 1, y_pos), (x_pos, y_pos + 1)

    def get_directions_from_start(self) -> list[tuple[int, int]]:
        connected = []
        dirs = [
            [self.start_x, self.start_y - 1],
            [self.start_x, self.start_y + 1],
            [self.start_x - 1, self.start_y],
            [self.start_x + 1, self.start_y]
        ]
        for d in dirs:
            if 0 < d[0] < len(self.field) - 1 and 0 < d[1] < len(self.field[0]) - 1 and self.field[d[0]][d[1]] != '.':
                for cell in self.get_directions(d[0], d[1]):
                    if cell == (self.start_x, self.start_y):
                        connected.append((d[0], d[1]))
                        break
        return connected


def do_loop(field: PipeField) -> int:
    start_x = field.start_x
    start_y = field.start_y
    steps_counter = 1
    prev_i, prev_j = start_x, start_y
    i = field.get_directions_from_start()[0][0]
    j = field.get_directions_from_start()[0][1]
    while i != start_x or j != start_y:
        directions = field.get_directions(i, j)
        for d in directions:
            if d != (prev_i, prev_j):
                break
        prev_i, prev_j = i, j
        i, j = d
        steps_counter += 1

    return steps_counter


def parse_input(input_path: str) -> list[list[str]]:
    result = []
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        for line in f:
            result.append([letter for letter in line])
    return result


def play(input_path: str):
    pipe_field = parse_input(input_path)
    field = PipeField(pipe_field)
    return do_loop(field) / 2


class TestPipes(unittest.TestCase):
    def test_get_directions(self):
        field = [
            ['.', '.', 'S', '.', '.'],
            ['.', 'F', '-', '7', '.'],
            ['.', '|', '.', '|', '.'],
            ['.', 'L', '-', 'J', '.'],
            ['.', '.', '.', '.', '.']
        ]
        pipe_field = PipeField(field)
        self.assertEqual(((3, 1), (3, 3)), pipe_field.get_directions(3, 2))  # '-' pipe
        self.assertEqual(((2, 1), (3, 2)), pipe_field.get_directions(3, 1))  # 'L' pipe
        self.assertEqual(((1, 1), (3, 1)), pipe_field.get_directions(2, 1))  # '|' pipe
        self.assertEqual(((2, 1), (1, 2)), pipe_field.get_directions(1, 1))  # 'F' pipe
        self.assertEqual(((2, 3), (1, 2)), pipe_field.get_directions(1, 3))  # '7' pipe
        self.assertEqual(((2, 3), (3, 2)), pipe_field.get_directions(3, 3))  # 'J' pipe

    def test_get_directions_from_start(self):
        field = [
            ['.', '.', '.', '.', '.'],
            ['.', 'F', '-', '7', '.'],
            ['.', '|', '.', '|', '.'],
            ['.', 'L', '-', 'S', '.'],
            ['.', '.', '.', '.', '.']
        ]
        pipe_field = PipeField(field)
        self.assertEqual([(3, 2), (2, 3)], pipe_field.get_directions_from_start())

    def test_do_loop(self):
        field = [
            ['.', '.', '.', '.', '.'],
            ['.', 'F', '-', '7', '.'],
            ['.', '|', '.', '|', '.'],
            ['.', 'L', '-', 'S', '.'],
            ['.', '.', '.', '.', '.']
        ]
        pipe_field = PipeField(field)
        self.assertEqual(8, do_loop(pipe_field))


if __name__ == '__main__':
    print(play('input_day_10.dat'))
