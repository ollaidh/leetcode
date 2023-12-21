import unittest
from dataclasses import dataclass


@dataclass
class SpringPack:
    springs: list[str]
    pattern: list[int]


def get_line_parameters(line: str) -> SpringPack:
    springs = list(line.split()[0])
    pattern = [int(letter) for letter in line.split()[1].split(',')]
    return SpringPack(springs, pattern)


def startswith_damaged(pack: list[str], number: int) -> bool:
    if not pack:
        return False
    for i in range(0, number - 1):
        if pack[i] != '#':
            return False
    if len(pack) > number and pack[number] == '#':
        return False
    return True


def check_pattern_match(pack: SpringPack):
    start = 0
    while pack.springs and pack.springs[0] != '#':
        pack.springs = pack.springs[1:]
    if not pack.springs and not pack.pattern:
        return True
    if not startswith_damaged(pack.springs[start:], pack.pattern[0]):
        return False
    pack.springs = pack.springs[pack.pattern[0]:]
    pack.pattern = pack.pattern[1:]
    return check_pattern_match(SpringPack(pack.springs, pack.pattern))


def count_arrangements(pack: SpringPack) -> int:
    result = 0
    if not pack.springs and not pack.pattern:
        return 1
    if pack.springs and not pack.pattern:
        return 0


class TestHotSprings(unittest.TestCase):
    def test_get_line_parameters(self):
        expected = SpringPack(['?', '?', '?', '.', '#', '#', '#'],
                              [1, 1, 3])
        self.assertEqual(expected, get_line_parameters("???.### 1,1,3"))

        expected = SpringPack(['?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?'],
                              [1, 3, 1, 6])
        self.assertEqual(expected, get_line_parameters("?#?#?#?#?#?#?#? 1,3,1,6"))

    def test_startswith_damaged(self):
        pack1 = ['#', '#', '#', '.', '.']
        self.assertTrue(startswith_damaged(pack1, 3))
        self.assertFalse(startswith_damaged(pack1, 2))

        pack2 = ['.', '#', '#', '.', '.']
        self.assertFalse(startswith_damaged(pack2, 2))

    def test_check_pattern_match(self):
        pack1 = SpringPack(
            ['#', '.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.'],
            [1, 6, 5])
        self.assertTrue(check_pattern_match(pack1))

        pack2 = SpringPack(
            ['.', '#', '.', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#'],
            [1, 3, 1, 6])
        self.assertTrue(check_pattern_match(pack2))

        pack3 = SpringPack(
            ['#', '.', '#', '.', '#', '#', '#'],
            [1, 1, 3])
        self.assertTrue(check_pattern_match(pack3))

    def test_count_arrangements(self):
        pack1 = SpringPack(
            ['?', '?', '?', '?', '.', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.'],
            [1, 6, 5])
        self.assertEqual(4, count_arrangements(pack1))

        pack2 = SpringPack(
            ['?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?'],
            [1, 3, 1, 6])
        self.assertEqual(1, count_arrangements(pack2))

        pack3 = SpringPack(
            ['?', '#', '#', '#', '?', '?', '?', '?', '?', '?', '?'],
            [3, 2, 1])
        self.assertEqual(10, count_arrangements(pack3))
