import unittest
from dataclasses import dataclass
import pathlib


@dataclass
class SpringPack:
    springs: str
    pattern: list[int]

    def __hash__(self):
        return hash((self.springs, tuple(self.pattern)))


def get_line_parameters(line: str, copies: int) -> SpringPack:
    springs = [line.split()[0]] * copies
    springs = '?'.join(springs)
    pattern = [int(letter) for letter in line.split()[1].split(',') * copies]
    return SpringPack(springs, pattern)


def replace_element(line: str, position: int) -> tuple[str, str]:
    if position >= len(line):
        stop = 0
    line_damaged = [c for c in line]
    line_operational = [c for c in line]
    line_damaged[position] = '#'
    line_operational[position] = '.'
    return ''.join(line_operational), ''.join(line_damaged)


def count_arrangements(pack: SpringPack, cache: dict) -> int:
    if pack in cache:
        return cache[pack]

    while pack.springs.startswith('.'):
        pack.springs = pack.springs[1:]

    if not pack.springs and not pack.pattern:
        return 1
    if not pack.springs and pack.pattern:
        return 0

    damaged_prefix_len = 0
    if pack.springs.startswith('#'):
        if not pack.pattern:
            return 0
        while damaged_prefix_len < len(pack.springs) and pack.springs[damaged_prefix_len] == "#":
            damaged_prefix_len += 1

        if damaged_prefix_len > pack.pattern[0]:
            return 0
        if damaged_prefix_len == len(pack.springs):
            if damaged_prefix_len != pack.pattern[0] or len(pack.pattern) > 1:
                return 0
            return 1

        #  '#' followed by '.':
        if pack.springs[damaged_prefix_len] == '.':
            if damaged_prefix_len != pack.pattern[0]:
                return 0
            pack.springs = pack.springs[damaged_prefix_len:]
            pack.pattern = pack.pattern[1:]
            result = count_arrangements(pack, cache)
            cache[pack] = result
            return result

    #  '#' followed by '?', or starts with '?':
    operational, damaged = replace_element(pack.springs, damaged_prefix_len)
    operational = SpringPack(operational, pack.pattern)
    damaged = SpringPack(damaged, pack.pattern)
    result_operational = count_arrangements(operational, cache)
    result_damaged = count_arrangements(damaged, cache)
    cache[operational] = result_operational
    cache[damaged] = result_damaged
    return result_operational + result_damaged


def play(input_path: str, copies: int) -> int:
    filepath_inp = pathlib.Path(__file__).parent.resolve() / input_path
    result = 0
    with open(filepath_inp) as f:
        line_index = 0
        for line in f:
            cache = {}
            result += count_arrangements(get_line_parameters(line, copies), cache)
            print('line:', line_index)
            line_index += 1

    return result


class TestHotSprings(unittest.TestCase):
    def test_get_line_parameters(self):
        expected = SpringPack('???.###',
                              [1, 1, 3])
        self.assertEqual(expected, get_line_parameters("???.### 1,1,3", 1))

        expected = SpringPack('?#?#?#?#?#?#?#?',
                              [1, 3, 1, 6])
        self.assertEqual(expected, get_line_parameters("?#?#?#?#?#?#?#? 1,3,1,6", 1))

    def test_count_arrangements(self):
        pack = SpringPack(
            '?',
            [1])
        self.assertEqual(1, count_arrangements(pack, {}))

        pack1 = SpringPack(
            '????.######..#####.',
            [1, 6, 5])
        self.assertEqual(4, count_arrangements(pack1, {}))

        pack2 = SpringPack(
            '?#?#?#?#?#?#?#?',
            [1, 3, 1, 6])
        self.assertEqual(1, count_arrangements(pack2, {}))

        pack3 = SpringPack(
            '?###????????',
            [3, 2, 1])
        self.assertEqual(10, count_arrangements(pack3, {}))

    def test_get_line_parameters_part2(self):
        expected = SpringPack('???.###????.###????.###????.###????.###',
                              [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3])
        self.assertEqual(expected, get_line_parameters("???.### 1,1,3", 5))


if __name__ == '__main__':
    print(play('inputs/test_day_12.dat', 1))
    print(play('inputs/test_day_12.dat', 5))
