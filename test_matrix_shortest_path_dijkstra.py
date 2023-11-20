# Given matrix n * m, where values are the prices to step into the cell,
# find the cheapest path from left up corner to right down corner
# Using Dijkstra algorithm


import unittest


class Node:
    def __init__(self, coords, length, parent=None):
        self.coords = coords
        self.length = length
        self.parent = parent

    def __eq__(self, other):
        if self or other:
            return False
        return self.coords == other.coords and self.length == other.length and self.parent == other.parent

    def __le__(self, other):
        return self.length <= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __str__(self):
        if self.parent:
            return f'[{self.coords}, {self.length}, parent: {self.parent.coords}]'
        return f'[{self.coords}, {self.length}, no parent]'

    def __hash__(self):
        return hash((self.coords, self.length, self.parent))


def min_path_node(nodes: set[Node]) -> Node:
    result = Node((0, 0), float('inf'))
    for node in nodes:
        result = min(result, node)
    return result


def get_neighbours(i: int, j: int, size_x: int, size_y: int) -> list[tuple]:
    result = []
    if j - 1 >= 0:
        result.append((i, j - 1))
    if j + 1 < size_y:
        result.append((i, j + 1))
    if i - 1 >= 0:
        result.append((i - 1, j))
    if i + 1 < size_x:
        result.append((i + 1, j))
    return result


def find_shortest_path(matrix: list[list[int]]) -> list[tuple]:
    curr = Node((0, 0), matrix[0][0])
    processed = {curr.coords}
    loops = {curr}
    matrix_size_x = len(matrix)
    matrix_size_y = len(matrix[0])
    while curr.coords != (matrix_size_x - 1, matrix_size_y - 1):
        neighbours = get_neighbours(curr.coords[0], curr.coords[1], matrix_size_x, matrix_size_y)
        for neigh in neighbours:
            if neigh not in processed:
                loops.add(
                    Node(
                        (neigh[0], neigh[1]), curr.length + matrix[neigh[0]][neigh[1]], curr
                    )
                )
                processed.add(
                    (neigh[0], neigh[1])
                )
        loops.remove(curr)
        curr = min_path_node(loops)
    result = []
    while curr.parent:
        result.append(curr.coords)
        curr = curr.parent
    return result[::-1]


class TestDijkstra(unittest.TestCase):
    def test_get_neighbours(self):
        result1 = get_neighbours(0, 0, 4, 4)
        self.assertEqual([(0, 1), (1, 0)], result1)

        result2 = get_neighbours(2, 2, 4, 4)
        self.assertEqual([(2, 1), (2, 3), (1, 2), (3, 2)], result2)

        result3 = get_neighbours(2, 2, 3, 4)
        self.assertEqual([(2, 1), (2, 3), (1, 2)], result3)

    def test_min_path_node(self):
        nodes1 = {
            Node((1, 1), 5),
            Node((1, 1), 2),
            Node((1, 1), 1),
            Node((1, 1), 10),
        }
        result1 = min_path_node(nodes1)
        self.assertEqual(1, result1.length)
        self.assertEqual((1, 1), result1.coords)

        nodes2 = {
            Node((1, 1), 5),
            Node((1, 1), 5),
        }
        result2 = min_path_node(nodes2)
        self.assertEqual(5, result2.length)
        self.assertEqual((1, 1), result2.coords)

    def test_find_shortest_path(self):
        matrix1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected1 = [(0, 1), (0, 2), (1, 2), (2, 2)]
        self.assertEqual(expected1, find_shortest_path(matrix1))

        matrix2 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected2 = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)]
        self.assertEqual(expected2, find_shortest_path(matrix2))

        matrix3 = [
            [1, 2],
            [3, 4]
        ]
        expected3 = [(0, 1), (1, 1)]
        self.assertEqual(expected3, find_shortest_path(matrix3))

        matrix4 = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [5, 5, 5, 5, 5, 5, 5, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 5, 5, 5, 5, 5, 5, 5],
            [1, 5, 5, 5, 5, 5, 5, 5],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [5, 5, 5, 5, 5, 5, 5, 1]
        ]
        expected4 = [(1, 0),
                      (2, 0),
                      (3, 0),
                      (4, 0),
                      (5, 0),
                      (5, 1),
                      (5, 2),
                      (5, 3),
                      (5, 4),
                      (5, 5),
                      (5, 6),
                      (5, 7),
                      (6, 7)]
        self.assertEqual(expected4, find_shortest_path(matrix4))
