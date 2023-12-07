import unittest
import pathlib


def parse_input(input_path: str) -> tuple[list[int], dict[str: list[dict[str, int]]]]:
    seeds = []
    deps = {}
    deps_types = {'seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:',
                  'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:'}
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with (open(filepath_inp) as f):
        file_lines = f.readlines()
        i = 0
        while i < len(file_lines):
            if file_lines[i].startswith('seeds'):
                line = file_lines[i].lstrip('seeds: ')
                line = line.rstrip()
                seeds = line.split()
                seeds = [int(seed) for seed in seeds]

            dep_type = file_lines[i].strip()
            if dep_type in deps_types:
                dep_type = dep_type.rstrip(' map:')
                i += 1
                deps[dep_type] = []
                while True:
                    try:
                        line = file_lines[i].strip()
                        line = line.split()
                        if not line:
                            break
                        deps[dep_type].append(
                            {'destination': int(line[0]), 'source': int(line[1]), 'range_length': int(line[2])})
                        i += 1
                    except IndexError:
                        break
            i += 1

    return seeds, deps


def get_destination(deps: list[dict[str, int]], value: int) -> int:
    for dep in deps:
        if dep['source'] <= value < dep['source'] + dep['range_length']:
            return dep['destination'] + (value - dep['source'])


def seed_location(seed: int, deps: dict[str: list[dict[str, int]]]) -> int:
    curr_parameter = seed
    for key in deps.keys():
        new_parameter = get_destination(deps[key], curr_parameter)
        if new_parameter is not None:
            curr_parameter = new_parameter
    return curr_parameter


def get_closest_location(seeds: list[int], deps: dict[str: list[dict[str, int]]]):
    closest = seed_location(seeds[0], deps)

    for seed in seeds:
        curr_location = seed_location(seed, deps)
        closest = min(closest, curr_location)

    return closest


class TestSeedSoil(unittest.TestCase):
    def test_get_destination(self):
        deps1 = [
            {'destination': 50, 'source': 98, 'range_length': 2},
            {'destination': 52, 'source': 50, 'range_length': 48}
        ]

        self.assertEqual(81, get_destination(deps1, 79))


if __name__ == '__main__':
    seeds, deps = parse_input('input_day_05_seeds_soils.dat')
    location = get_closest_location(seeds, deps)
    print(location)



