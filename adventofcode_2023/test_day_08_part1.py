import unittest
import pathlib


def line_to_node(line: str) -> tuple[str, list[str]]:
    line = line.split()
    node_name = line[0]
    left = line[2].lstrip('(').rstrip(',')
    right = line[3].rstrip(')')
    return node_name, [left, right]


def parse_input(input_path: str) -> tuple[str, dict[str, list[str]]]:
    nodes = {}
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        directions = file_lines[0]
        for i in range(2, len(file_lines)):
            node_name, instructions = line_to_node(file_lines[i])
            nodes[node_name] = instructions
    return directions, nodes


def escape(directions: str, nodes: dict[str, list[str]]) -> int:
    steps = 0
    directions_length = len(directions)
    i = 0
    curr = 'AAA'
    while True:
        if directions[i] == "L":
            curr = nodes[curr][0]
        else:
            curr = nodes[curr][1]
        steps += 1
        if curr == 'ZZZ':
            break
        i += 1
        if i == directions_length - 1:
            i = 0
    return steps


def play(input_path: str) -> int:
    directions, nodes = parse_input(input_path)
    return escape(directions, nodes)


class TestHauntedWasteland(unittest.TestCase):
    def test_line_to_node(self):
        node_name, instructions = line_to_node('AAA = (BBB, CCC)')
        self.assertEqual('AAA', node_name)
        self.assertEqual(['BBB', 'CCC'], instructions)

    def test_escape(self):
        directions = 'LLR'
        nodes = {
            'AAA': ['BBB', 'BBB'],
            'BBB': ['AAA', 'ZZZ'],
            'ZZZ': ['ZZZ', 'ZZZ']
        }
        self.assertEqual(6, escape(directions, nodes))

        directions = 'RL'
        nodes = {
            'AAA': ['BBB', 'CCC'],
            'BBB': ['DDD', 'EEE'],
            'CCC': ['ZZZ', 'GGG'],
            'DDD': ['DDD', 'DDD'],
            'EEE': ['EEE', 'EEE'],
            'GGG': ['GGG', 'GGG'],
            'ZZZ': ['ZZZ', 'ZZZ']
        }
        self.assertEqual(2, escape(directions, nodes))


if __name__ == '__main__':
    result = play('input_day_08_part1.dat')
    print(result)
