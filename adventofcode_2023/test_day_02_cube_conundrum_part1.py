# Bag contains some cubes which are either red, green, or blue.
# Elf will reach into the bag, grab a handful of random cubes, show them to you,
# and then put them back in the bag. He'll do this a few times per game.
#
# You play several games and record the information from each game.
# Each game is listed with its ID number (like the 11 in Game 11: ...)
# followed by a semicolon-separated list of subsets of cubes that were revealed from the bag
# (like 3 red, 5 green, 4 blue).

# The Elf would first like to know which games would have been possible if the bag contained
# only 12 red cubes, 13 green cubes, and 14 blue cubes?


import unittest
from dataclasses import dataclass
import pathlib


@dataclass
class CubesPack:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __gt__(self, other):
        if self.red > other.red or self.green > other.green or self.blue > other.blue:
            return True
        return False


def play_game(game_id: int, cube_packs: list[CubesPack], base_pack: CubesPack) -> int:
    for pack in cube_packs:
        if pack > base_pack:
            return 0
    return game_id


def get_game_parameters(game: str) -> tuple[int, list[CubesPack]]:
    cubes_packs = []
    game = game.rstrip().lstrip("Game ")
    game = game.split(":")
    game_id = int(game[0])
    games = game[1].split(";")
    for game in games:
        cubes = game.split(",")
        pack = CubesPack()
        for cube in cubes:
            cube = cube.lstrip().split()
            if cube[1] == 'red':
                pack.red = int(cube[0])
            if cube[1] == 'green':
                pack.green = int(cube[0])
            if cube[1] == 'blue':
                pack.blue = int(cube[0])
        cubes_packs.append(pack)
    return game_id, cubes_packs


def play(input_path: str, base_pack: CubesPack):
    ids_sum = 0

    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        for line in file_lines:
            game_id, cubes_packs = get_game_parameters(line)
            ids_sum += play_game(game_id, cubes_packs, base_pack)
    return ids_sum


class TestCubeConundrum(unittest.TestCase):
    def test_compare_cubes_packs(self):
        self.assertTrue(CubesPack(1, 2, 3) > CubesPack(1, 1, 1))
        self.assertFalse(CubesPack(1, 2, 3) > CubesPack(111, 111, 111))

    def test_play_game(self):
        packs = [CubesPack(1, 2, 3), CubesPack(2, 12, 4), CubesPack(3, 3, 3)]
        self.assertEqual(0, play_game(1, packs, CubesPack(1, 12, 10)))
        self.assertEqual(2, play_game(2, packs, CubesPack(100, 100, 100)))

    def test_get_game_parameters(self):
        game = ("Game 31: 3 blue, 7 green, 10 red; 4 green, 4 red; 1 green, 7 blue, 5 red;"
                "8 blue, 10 red; 7 blue,19 red, 1 green")
        game_id, packs = get_game_parameters(game)
        self.assertEqual(31, game_id)
        expected_packs = [
            CubesPack(10, 7, 3),
            CubesPack(4, 4, 0),
            CubesPack(5, 1, 7),
            CubesPack(10, 0, 8),
            CubesPack(19, 1, 7)
        ]
        self.assertEqual(expected_packs, packs)

    def test_play(self):
        input_path = 'input_day_02_cube_conundrum.dat'
        base_pack = CubesPack(12, 13, 14)
        self.assertEqual(2162, play(input_path, base_pack))

