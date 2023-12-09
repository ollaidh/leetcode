import unittest
import pathlib


def solve_one_history(seq: list[int]) -> int:
    if all(x == 0 for x in seq):
        return 0
    new_seq = []
    for i in range(len(seq) - 1):
        new_seq.append(seq[i + 1] - seq[i])
    return solve_one_history(new_seq) + seq[-1]


def parse_input(input_path: str) -> list[list[int]]:
    result = []
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        for line in f:
            result.append([int(number) for number in line.split()])
    return result


def play(input_path: str) -> int:
    result = 0
    histories = parse_input(input_path)
    for history in histories:
        result += solve_one_history(history)
    return result


class TestSolve(unittest.TestCase):
    def test_solve_one_history(self):
        input_seq2 = [1,   3,   6,  10,  15,  21]
        self.assertEqual(28, solve_one_history(input_seq2))

        input_seq2 = [10,  13,  16,  21,  30,  45]
        self.assertEqual(68, solve_one_history(input_seq2))


if __name__ == '__main__':
    print(play('input_day_09.dat'))
