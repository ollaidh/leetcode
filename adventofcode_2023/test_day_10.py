import unittest
import pathlib


class PipeField:
    def __init__(self, field: list[list[str]]):
        self.field = field
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
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

    def type_start_pipe(self, start_directions):
        dir_1 = start_directions[0]
        dir_2 = start_directions[1]
        if dir_1[0] == dir_2[0]:
            self.field[self.start_x][self.start_y] = "-"
        elif dir_1[1] == dir_2[1]:
            self.field[self.start_x][self.start_y] = "|"
        elif dir_1[0] == dir_2[0] + 1 and dir_1[1] == dir_2[1] + 1:
            self.field[self.start_x][self.start_y] = "L"
        elif dir_1[0] == dir_2[0] + 1 and dir_1[1] == dir_2[1] - 1:
            self.field[self.start_x][self.start_y] = "J"
        elif dir_1[0] == dir_2[0] - 1 and dir_1[1] == dir_2[1] - 1:
            self.field[self.start_x][self.start_y] = "7"
        elif dir_1[0] == dir_2[0] - 1 and dir_1[1] == dir_2[1] + 1:
            self.field[self.start_x][self.start_y] = "F"


def do_loop(field: PipeField) -> dict[tuple[int, int]: str]:
    start_x = field.start_x
    start_y = field.start_y
    result = {(start_x, start_y): field.field[start_x][start_y]}
    prev_i, prev_j = start_x, start_y
    i = field.get_directions_from_start()[0][0]
    j = field.get_directions_from_start()[0][1]
    while i != start_x or j != start_y:
        result[(i, j)] = field.field[i][j]

        directions = field.get_directions(i, j)
        for d in directions:
            if d != (prev_i, prev_j):
                break
        prev_i, prev_j = i, j
        i, j = d
    return result


def check_point_inside_loop(x_point: int, y_point: int, loop: dict[tuple[int, int]: str],
                            x_max: int, y_max: int) -> bool:
    intersections = 0
    i, j = x_point + 1, y_point + 1
    while i <= x_max and j <= y_max:
        if (i, j) in loop and loop[(i, j)] != "7" and loop[(i, j)] != "L":
            intersections += 1
        i += 1
        j += 1

    return intersections % 2 != 0


def calc_enclosed_points(loop: dict[tuple[int, int]: str]) -> int:
    result = 0
    x_coords = [point[0] for point in loop]
    y_coords = [point[1] for point in loop]
    x_min = min(x_coords)
    x_max = max(x_coords)
    y_min = min(y_coords)
    y_max = max(y_coords)

    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if (i, j) not in loop:
                result += check_point_inside_loop(i, j, loop, x_max, y_max)
    return result


def parse_input(input_path: str) -> list[list[str]]:
    result = []
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        for line in f:
            result.append([letter for letter in line])
    return result


def play_1(input_path: str):
    pipe_field = parse_input(input_path)
    field = PipeField(pipe_field)
    return len(do_loop(field)) / 2


def play_2(input_path: str):
    pipe_field = parse_input(input_path)
    field = PipeField(pipe_field)
    field.type_start_pipe(field.get_directions_from_start())
    loop = do_loop(field)
    return calc_enclosed_points(loop)


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
        pipe_field.type_start_pipe([(3, 2), (2, 3)])
        result = do_loop(pipe_field)
        expected = {
            (3, 3): "J", (3, 2): "-", (3, 1): "L", (2, 1): "|",
            (1, 1): "F", (1, 2): "-", (1, 3): "7", (2, 3): "|"
        }
        print(result)
        self.assertEqual(8, len(do_loop(pipe_field)))
        self.assertEqual(expected, result)

    def test_type_start_pipe(self):
        field = [
            ['.', '.', '.', '.', '.'],
            ['.', 'F', '-', '7', '.'],
            ['.', '|', '.', '|', '.'],
            ['.', 'L', '-', 'J', '.'],
            ['.', '.', '.', '.', '.']
        ]
        pipe_field = PipeField(field)

        pipe_field.start_x, pipe_field.start_y = 1, 2
        pipe_field.field[pipe_field.start_x][pipe_field.start_y] = "S"
        pipe_field.type_start_pipe(pipe_field.get_directions_from_start())
        self.assertEqual("-", pipe_field.field[pipe_field.start_x][pipe_field.start_y])

        pipe_field.start_x, pipe_field.start_y = 2, 1
        pipe_field.field[pipe_field.start_x][pipe_field.start_y] = "S"
        pipe_field.type_start_pipe(pipe_field.get_directions_from_start())
        self.assertEqual("|", pipe_field.field[pipe_field.start_x][pipe_field.start_y])

        pipe_field.start_x, pipe_field.start_y = 3, 1
        pipe_field.field[pipe_field.start_x][pipe_field.start_y] = "S"
        pipe_field.type_start_pipe(pipe_field.get_directions_from_start())
        self.assertEqual("L", pipe_field.field[pipe_field.start_x][pipe_field.start_y])

        pipe_field.start_x, pipe_field.start_y = 3, 3
        pipe_field.field[pipe_field.start_x][pipe_field.start_y] = "S"
        pipe_field.type_start_pipe(pipe_field.get_directions_from_start())
        self.assertEqual("J", pipe_field.field[pipe_field.start_x][pipe_field.start_y])

        pipe_field.start_x, pipe_field.start_y = 1, 3
        pipe_field.field[pipe_field.start_x][pipe_field.start_y] = "S"
        pipe_field.type_start_pipe(pipe_field.get_directions_from_start())
        self.assertEqual("7", pipe_field.field[pipe_field.start_x][pipe_field.start_y])

        pipe_field.start_x, pipe_field.start_y = 1, 1
        pipe_field.field[pipe_field.start_x][pipe_field.start_y] = "S"
        pipe_field.type_start_pipe(pipe_field.get_directions_from_start())
        self.assertEqual("F", pipe_field.field[pipe_field.start_x][pipe_field.start_y])

    def test_check_point_inside_loop(self):
        loop = {
            (3, 3): "J", (3, 2): "-", (3, 1): "L", (2, 1): "|",
            (1, 1): "F", (1, 2): "-", (1, 3): "7", (2, 3): "|"
        }
        x_max, y_max = 3, 3

        self.assertTrue(check_point_inside_loop(2, 2, loop, x_max, y_max))
        self.assertFalse(check_point_inside_loop(3, 3, loop, x_max, y_max))
        self.assertFalse(check_point_inside_loop(3, 0, loop, x_max, y_max))

        field = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', 'S', '-', '-', '-', '-', '-', '-', '-', '7', '.'],
            ['.', '|', 'F', '-', '-', '-', '-', '-', '7', '|', '.'],
            ['.', '|', '|', '.', '.', '.', '.', '.', '|', '|', '.'],
            ['.', '|', '|', '.', '.', '.', '.', '.', '|', '|', '.'],
            ['.', '|', 'L', '-', '7', '.', 'F', '-', 'J', '|', '.'],
            ['.', '|', '.', '.', '|', '.', '|', '.', '.', '|', '.'],
            ['.', 'L', '-', '-', 'J', '.', 'L', '-', '-', 'J', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ]
        pipe_field = PipeField(field)
        dirs = pipe_field.get_directions_from_start()
        pipe_field.type_start_pipe(dirs)
        loop = do_loop(pipe_field)
        self.assertTrue(check_point_inside_loop(6, 2, loop, 9, 11))

        field = [
            ['.', 'F', '-', '-', '-', '-', '7', 'F', '7', 'F', '7', 'F', '7', 'F', '-', '7', '.', '.', '.', '.'],
            ['.', '|', 'F', '-', '-', '7', '|', '|', '|', '|', '|', '|', '|', '|', 'F', 'J', '.', '.', '.', '.'],
            ['.', '|', '|', '.', 'F', 'J', '|', '|', '|', '|', '|', '|', '|', '|', 'L', '7', '.', '.', '.', '.'],
            ['F', 'J', 'L', '7', 'L', '7', 'L', 'J', 'L', 'J', '|', '|', 'L', 'J', '.', 'L', '-', '7', '.', '.'],
            ['L', '-', '-', 'J', '.', 'L', '7', '.', '.', '.', 'L', 'J', 'S', '7', 'F', '-', '7', 'L', '7', '.'],
            ['.', '.', '.', '.', 'F', '-', 'J', '.', '.', 'F', '7', 'F', 'J', '|', 'L', '7', 'L', '7', 'L', '7'],
            ['.', '.', '.', '.', 'L', '7', '.', 'F', '7', '|', '|', 'L', '7', '|', '.', 'L', '7', 'L', '7', '|'],
            ['.', '.', '.', '.', '.', '|', 'F', 'J', 'L', 'J', '|', 'F', 'J', '|', 'F', '7', '|', '.', 'L', 'J'],
            ['.', '.', '.', '.', 'F', 'J', 'L', '-', '7', '.', '|', '|', '.', '|', '|', '|', '|', '.', '.', '.'],
            ['.', '.', '.', '.', 'L', '-', '-', '-', 'J', '.', 'L', 'J', '.', 'L', 'J', 'L', 'J', '.', '.', '.']
        ]
        pipe_field = PipeField(field)
        dirs = pipe_field.get_directions_from_start()
        pipe_field.type_start_pipe(dirs)
        loop = do_loop(pipe_field)
        self.assertTrue(check_point_inside_loop(4, 7, loop, 10, 20))

    def test_calc_enclosed_points(self):
        field = [
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', 'S', '-', '-', '-', '-', '-', '-', '-', '7', '.'],
            ['.', '|', 'F', '-', '-', '-', '-', '-', '7', '|', '.'],
            ['.', '|', '|', '.', '.', '.', '.', '.', '|', '|', '.'],
            ['.', '|', '|', '.', '.', '.', '.', '.', '|', '|', '.'],
            ['.', '|', 'L', '-', '7', '.', 'F', '-', 'J', '|', '.'],
            ['.', '|', '.', '.', '|', '.', '|', '.', '.', '|', '.'],
            ['.', 'L', '-', '-', 'J', '.', 'L', '-', '-', 'J', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ]
        pipe_field = PipeField(field)
        dirs = pipe_field.get_directions_from_start()
        pipe_field.type_start_pipe(dirs)
        loop = do_loop(pipe_field)
        result = calc_enclosed_points(loop)
        self.assertEqual(4, result)

        field = [
            ['.', 'F', '-', '-', '-', '-', '7', 'F', '7', 'F', '7', 'F', '7', 'F', '-', '7', '.', '.', '.', '.'],
            ['.', '|', 'F', '-', '-', '7', '|', '|', '|', '|', '|', '|', '|', '|', 'F', 'J', '.', '.', '.', '.'],
            ['.', '|', '|', '.', 'F', 'J', '|', '|', '|', '|', '|', '|', '|', '|', 'L', '7', '.', '.', '.', '.'],
            ['F', 'J', 'L', '7', 'L', '7', 'L', 'J', 'L', 'J', '|', '|', 'L', 'J', '.', 'L', '-', '7', '.', '.'],
            ['L', '-', '-', 'J', '.', 'L', '7', '.', '.', '.', 'L', 'J', 'S', '7', 'F', '-', '7', 'L', '7', '.'],
            ['.', '.', '.', '.', 'F', '-', 'J', '.', '.', 'F', '7', 'F', 'J', '|', 'L', '7', 'L', '7', 'L', '7'],
            ['.', '.', '.', '.', 'L', '7', '.', 'F', '7', '|', '|', 'L', '7', '|', '.', 'L', '7', 'L', '7', '|'],
            ['.', '.', '.', '.', '.', '|', 'F', 'J', 'L', 'J', '|', 'F', 'J', '|', 'F', '7', '|', '.', 'L', 'J'],
            ['.', '.', '.', '.', 'F', 'J', 'L', '-', '7', '.', '|', '|', '.', '|', '|', '|', '|', '.', '.', '.'],
            ['.', '.', '.', '.', 'L', '-', '-', '-', 'J', '.', 'L', 'J', '.', 'L', 'J', 'L', 'J', '.', '.', '.']
        ]
        pipe_field = PipeField(field)
        dirs = pipe_field.get_directions_from_start()
        pipe_field.type_start_pipe(dirs)
        loop = do_loop(pipe_field)
        result = calc_enclosed_points(loop)
        self.assertEqual(8, result)


if __name__ == '__main__':
    print(play_2('input_day_10.dat'))
