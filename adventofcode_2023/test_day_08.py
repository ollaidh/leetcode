import unittest
import pathlib
from math import gcd

def line_to_node(line: str) -> tuple[str, list[str]]:
    line = line.split()
    node_name = line[0]
    left = line[2].lstrip('(').rstrip(',')
    right = line[3].rstrip(')')
    return node_name, [left, right]


def parse_input(input_path: str) -> tuple[str, dict[str, list[str]], list[str]]:
    nodes = {}
    starts = []
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        directions = file_lines[0]
        for i in range(2, len(file_lines)):
            node_name, instructions = line_to_node(file_lines[i])
            nodes[node_name] = instructions
            if node_name.endswith('A'):
                starts.append(node_name)
    return directions, nodes, starts


def escape(directions: str, nodes: dict[str, list[str]], starts: list[str]) -> list[int]:
    directions_length = len(directions)
    all_steps = []
    for curr in starts:
        steps = 0
        i = 0
        while True:
            if directions[i] == "L":
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]
            steps += 1
            if curr.endswith('Z'):
                break
            i += 1
            if i == directions_length - 1:
                i = 0
        all_steps.append(steps)
    return all_steps


def play(input_path: str) -> int:
    directions, nodes, starts = parse_input(input_path)
    steps = escape(directions, nodes, starts)
    lcm = 1
    for i in steps:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


class TestHauntedWasteland(unittest.TestCase):
    def test_line_to_node(self):
        node_name, instructions = line_to_node('AAA = (BBB, CCC)')
        self.assertEqual('AAA', node_name)
        self.assertEqual(['BBB', 'CCC'], instructions)
        self.assertTrue([True, False, True])

    # def test_escape(self):
    #     directions = 'LR'
    #     nodes = {
    #         '11A': ['11B', 'XXX'],
    #         '11B': ['XXX', '11Z'],
    #         '11Z': ['11B', 'XXX'],
    #         '22A': ['22B', 'XXX'],
    #         '22B': ['22C', '22C'],
    #         '22C': ['22Z', '22Z'],
    #         '22Z': ['22B', '22B'],
    #         'XXX': ['XXX', 'XXX']
    #     }
    #     starts = ['11A', '22A']
    #     self.assertEqual(6, escape(directions, nodes, starts))


if __name__ == '__main__':
    result = play('input_day_08_part1.dat')
    print(result)

# class TestHauntedWasteland(unittest.TestCase):
#     def test_line_to_node(self):
#         node_name, instructions = line_to_node('AAA = (BBB, CCC)')
#         self.assertEqual('AAA', node_name)
#         self.assertEqual(['BBB', 'CCC'], instructions)
#
#     def test_escape(self):
#         directions = 'LLR'
#         nodes = {
#             'AAA': ['BBB', 'BBB'],
#             'BBB': ['AAA', 'ZZZ'],
#             'ZZZ': ['ZZZ', 'ZZZ']
#         }
#         self.assertEqual(6, escape(directions, nodes))
#
#         directions = 'RL'
#         nodes = {
#             'AAA': ['BBB', 'CCC'],
#             'BBB': ['DDD', 'EEE'],
#             'CCC': ['ZZZ', 'GGG'],
#             'DDD': ['DDD', 'DDD'],
#             'EEE': ['EEE', 'EEE'],
#             'GGG': ['GGG', 'GGG'],
#             'ZZZ': ['ZZZ', 'ZZZ']
#         }
#         self.assertEqual(2, escape(directions, nodes))
#
#
# if __name__ == '__main__':
#     result = play('input_day_08_part1.dat')
#     print(result)


# def escape(directions: str, nodes: dict[str, list[str]], starts: list[str]) -> int:
#     directions_length = len(directions)
#     backup_starts = starts
#     visited = set()
#     i = 0
#     while True:
#         curr = []
#         ends_with_z = True
#         print(starts[0])
#         if starts[0] in visited:
#             print(starts[0], backup_starts[0])
#             break
#         else:
#             visited.add(starts[0])
#         for start in starts:
#             if directions[i] == "L":
#                 curr.append(nodes[start][0])
#             else:
#                 curr.append(nodes[start][1])
#             if curr[-1].endswith('Z') is False:
#                 ends_with_z = False
#         i += 1
#         if ends_with_z is True:
#             break
#         starts = curr
#         if i == directions_length:
#             i = 0
#     return 0