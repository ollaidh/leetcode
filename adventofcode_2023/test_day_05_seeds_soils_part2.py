import unittest
import pathlib
from dataclasses import dataclass
import datetime
import cProfile
import pstats


@dataclass
class Bucket:
    destination: int
    source: int
    interval: int


@dataclass
class Map:
    name: str
    buckets: list[Bucket]


def parse_input(input_path: str) -> tuple[list[int], list[Map]]:
    seeds = []
    deps = []
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
                dep = Map(dep_type, [])
                while True:
                    try:
                        line = file_lines[i].strip()
                        line = line.split()
                        if not line:
                            break
                        dep.buckets.append(Bucket(int(line[0]), int(line[1]), int(line[2])))
                        i += 1
                    except IndexError:
                        break
                deps.append(dep)
            i += 1

    return seeds, deps


def get_destination(dep: Map, value: int) -> int:
    for i, _ in enumerate(dep.buckets):
        if dep.buckets[i].source <= value < dep.buckets[i].source + dep.buckets[i].interval:
            return dep.buckets[i].destination + (value - dep.buckets[i].source)


def seed_location(seed: int, deps: list[Map]) -> int:
    curr_parameter = seed
    for dep in deps:
        new_parameter = get_destination(dep, curr_parameter)
        if new_parameter is not None:
            curr_parameter = new_parameter
    return curr_parameter


def get_closest_location(seeds: list[int], deps: list[Map]):
    print('START Time:', datetime.datetime.now().time())

    closest = seed_location(seeds[0], deps)
    i = 0
    while i <= len(seeds) - 1:
        for j in range(seeds[i], seeds[i] + seeds[i + 1]):
            # print(j, 'Bucket:', seeds[i], seeds[i] + seeds[i + 1], '    Time:', datetime.datetime.now().time())

            curr_location = seed_location(j, deps)
            closest = min(closest, curr_location)
            j += 1
        print('Bucket:', seeds[i], seeds[i] + seeds[i + 1], '    Time:', datetime.datetime.now().time())
        i += 2
        break

    return closest


class TestSeedSoil(unittest.TestCase):
    def test_get_destination(self):
        deps1 = Map('dep1', [Bucket(50, 98, 2), Bucket(52, 50, 48)])
        self.assertEqual(81, get_destination(deps1, 79))

    def test_get_closest_location(self):
        sds = [79, 14, 55, 13]
        dps = [
            Map('seed - to - soil', [Bucket(50, 98, 2), Bucket(52, 50, 48)]),
            Map('soil - to - fertilizer', [Bucket(0, 15, 37), Bucket(37, 52, 2), Bucket(39, 0, 15)]),
            Map('fertilizer - to - water', [Bucket(49, 53, 8), Bucket(0, 11, 42), Bucket(42, 0, 7), Bucket(57, 7, 4)]),
            Map('water - to - light', [Bucket(88, 18, 7), Bucket(18, 25, 70)]),
            Map('light - to - temperature', [Bucket(45, 77, 23), Bucket(81, 45, 19), Bucket(68, 64, 13)]),
            Map('temperature - to - humidity', [Bucket(0, 69, 1), Bucket(1, 0, 69)]),
            Map('humidity - to - location', [Bucket(60, 56, 37), Bucket(56, 93, 4)])
        ]

        self.assertEqual(46, get_closest_location(sds, dps))


if __name__ == '__main__':
    with cProfile.Profile() as profile:
        seeds, deps = parse_input('input_day_05_seeds_soils.dat')
        location = get_closest_location(seeds, deps)
        print(location)

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
    results.dump_stats('results_2.prof')



