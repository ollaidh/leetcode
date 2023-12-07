import unittest
import pathlib


def parse_input(input_path: str) -> tuple[list[int], list[int]]:
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        times = [int(i) for i in file_lines[0].lstrip('Time:').lstrip().rstrip().split()]
        distances = [int(i) for i in file_lines[1].lstrip('Distance:').lstrip().rstrip().split()]
        return times, distances


def race_count_winning_cases(time: int, best_distance: int) -> int:
    counter = 0
    for t in range(time):
        distance = t * time - t * t
        counter += distance > best_distance
    return counter


def mult_winning_cases(times: list[int], best_dictances: list[int]) -> int:
    mult_winning = 1
    for time, best_distance in zip(times, best_dictances):
        mult_winning *= race_count_winning_cases(time, best_distance)

    return mult_winning


def race(input_path: str) -> int:
    times, best_distances = parse_input(input_path)
    return mult_winning_cases(times, best_distances)


class TestWaitForIt(unittest.TestCase):
    def test_race_count_winning_cases(self):
        self.assertEqual(4, race_count_winning_cases(7, 9))
        self.assertEqual(8, race_count_winning_cases(15, 40))
        self.assertEqual(9, race_count_winning_cases(30, 200))

    def test_mult_winning_cases(self):
        times = [7, 15, 30]
        best_distances = [9, 40, 200]
        self.assertEqual(288, mult_winning_cases(times, best_distances))

    # def test_mult_winning_cases_input(self):
    #     result = race('input_day_06_waitforit.dat')
    #     self.assertEqual(503424, result)
