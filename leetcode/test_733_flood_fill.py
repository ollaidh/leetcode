import unittest


def get_neighbours(i: int, j: int, matrix: list[list[int]], color: int) -> list[tuple]:
    result = []
    size_x = len(matrix)
    size_y = len(matrix[0])
    if j - 1 >= 0 and matrix[i][j] == color:
        result.append((i, j - 1))
    if j + 1 < size_y and matrix[i][j] == color:
        result.append((i, j + 1))
    if i - 1 >= 0 and matrix[i][j] == color:
        result.append((i - 1, j))
    if i + 1 < size_x and matrix[i][j] == color:
        result.append((i + 1, j))
    return result


class TestSolution(unittest.TestCase):
    def test_get_neighbours(self):
        pass