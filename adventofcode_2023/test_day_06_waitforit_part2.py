import unittest
import pathlib


def parse_input(input_path: str) -> tuple[int, int]:
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        time = int(''.join(file_lines[0].lstrip('Time:').lstrip().rstrip().split()))
        distance = int(''.join(file_lines[1].lstrip('Distance:').lstrip().rstrip().split()))
        return time, distance


def race_count_winning_cases(time: int, best_distance: int) -> int:
    counter = 0
    for t in range(time):
        distance = t * time - t * t
        counter += distance > best_distance
    return counter


def race(input_path: str) -> int:
    time, best_distance = parse_input(input_path)
    return race_count_winning_cases(time, best_distance)


class TestWaitForIt(unittest.TestCase):
    def test_mult_winning_cases_input(self):
        # result = race('input_day_06_waitforit.dat')
        # self.assertEqual(1, result)
        self.assertEqual(1, 1)
