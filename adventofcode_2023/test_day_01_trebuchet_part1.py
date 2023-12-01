# Document consists of lines of text
# On each line, the calibration value can be found by combining the first digit
# and the last digit (in that order) to form a single two-digit number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# Calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.


import unittest
import pathlib

digits_numerical = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_first_digit(line: str) -> str:
    for letter in line:
        if letter in digits_numerical:
            return letter


def get_last_digit(line: str) -> str:
    for i in range(len(line) - 1, -1, -1):
        if line[i] in digits_numerical:
            return line[i]


def get_calibration_value(line: str):
    ld = get_first_digit(line)
    rd = get_last_digit(line)
    return int(f'{ld}{rd}')


def trebuchet(input_path: str):
    calibration_sum = 0

    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        for line in file_lines:
            calibration_sum += get_calibration_value(line)

    return calibration_sum


class TestTrebuchet(unittest.TestCase):
    def test_get_calibration_value(self):
        self.assertEqual(12, get_calibration_value('jvb1sdvk4kn5t2ngrlbt'))
        self.assertEqual(55, get_calibration_value('dfkjn0knnbr5lbnbs'))
        self.assertEqual(31, get_calibration_value('kbsv3lkdsrbn5dbljnr5ffe46knbv1'))
        self.assertEqual(55, get_calibration_value('dfvb5kdnb'))
        self.assertEqual(22, get_calibration_value('abcoe2theexyz'))
        self.assertEqual(99, get_calibration_value('9pc'))

    def test_trebuchet(self):
        self.assertEqual(53974, trebuchet('input_day_01_trebuchet.dat'))


