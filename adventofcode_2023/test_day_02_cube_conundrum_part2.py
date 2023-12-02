# In each game you played, what is the fewest number of cubes of each color
# that could have been in the bag to make the game possible?
# The power of a set of cubes is equal to the numbers of red, green, and
# blue cubes multiplied together.
# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?


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


def game_cubes_power(cube_packs: list[CubesPack]) -> int:
    fewest_cubes_pack = CubesPack()
    for pack in cube_packs:
        fewest_cubes_pack.red = max(fewest_cubes_pack.red, pack.red)
        fewest_cubes_pack.green = max(fewest_cubes_pack.green, pack.green)
        fewest_cubes_pack.blue = max(fewest_cubes_pack.blue, pack.blue)
    return fewest_cubes_pack.red * fewest_cubes_pack.green * fewest_cubes_pack.blue


def get_game_parameters(game: str) -> list[CubesPack]:
    cubes_packs = []
    game = game.rstrip().lstrip("Game ")
    game = game.split(":")
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
    return cubes_packs


def play(input_path: str):
    ids_sum = 0
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        for line in file_lines:
            cubes_packs = get_game_parameters(line)
            ids_sum += game_cubes_power(cubes_packs)
    return ids_sum


class TestCubeConundrum(unittest.TestCase):
    def test_game_cubes_power(self):
        packs1 = [CubesPack(1, 2, 3), CubesPack(2, 12, 4), CubesPack(3, 3, 3)]
        self.assertEqual(144, game_cubes_power(packs1))
        packs2 = [CubesPack(0, 2, 3), CubesPack(0, 12, 4), CubesPack(0, 3, 3)]
        self.assertEqual(0, game_cubes_power(packs2))

    def test_play(self):
        input_path = 'input_day_02_cube_conundrum.dat'
        self.assertEqual(72513, play(input_path))

