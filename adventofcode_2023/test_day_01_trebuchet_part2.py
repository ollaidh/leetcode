# Add to part 1: Now some of the digits are actually spelled out with letters:
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
#
# Find the real first and last digit on each line. For example:
#
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.


import unittest
import pathlib

digits_numerical = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
digits_string = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                 "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def get_first_digit(line: str) -> str:
    while line:
        if line[0] in digits_numerical:
            return line[0]
        for digit in digits_string.keys():
            if line.startswith(digit):
                return digits_string[digit]
        line = line[1:]


def get_last_digit(line: str) -> str:
    while line:
        if line[-1] in digits_numerical:
            return line[-1]
        for digit in digits_string.keys():
            if line.endswith(digit):
                return digits_string[digit]
        line = line[:-1]


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
        self.assertEqual(12, get_calibration_value('jvbonesdvk4kn5ttwongrlbt'))
        self.assertEqual(55, get_calibration_value('dfkjn0knnbr5lbnbs'))
        self.assertEqual(55, get_calibration_value('dfkjn0knnbrfivelbnbs'))
        self.assertEqual(31, get_calibration_value('kbsv3lkdsrbn5dbljnr5ffe46knbv1'))
        self.assertEqual(31, get_calibration_value('kbthreesv3lkdsrbn5dbljnr5ffe46knbv1'))
        self.assertEqual(55, get_calibration_value('dfvb5kdnb'))
        self.assertEqual(29, get_calibration_value('two1nine'))
        self.assertEqual(83, get_calibration_value('eightwothree'))
        self.assertEqual(13, get_calibration_value('abcone2threexyz'))
        self.assertEqual(24, get_calibration_value('xtwone3four'))
        self.assertEqual(92, get_calibration_value('nineeightseven2'))
        self.assertEqual(14, get_calibration_value('zoneight234'))
        self.assertEqual(76, get_calibration_value('7pqrstsixteen'))

        self.assertEqual(18, get_calibration_value('oneight'))
        self.assertEqual(99, get_calibration_value('9pc'))

    def test_trebuchet(self):
        self.assertEqual(52840, trebuchet('input_day_01_trebuchet.dat'))


