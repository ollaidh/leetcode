# You are given row x col grid representing a map where grid[i][j] = 1 represents land
# and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally).
# The grid is completely surrounded by water, and there is exactly one island.
# The island doesn't have "lakes"


import unittest
from my_utils.utils import get_neighbours


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        result = 0

        size_x = len(grid)
        size_y = len(grid[0])

        start = (0, 0)
        for i in range(size_x):
            found = False
            for j in range(size_y):
                if grid[i][j] == 1:
                    start = (i, j)
                    found = True
                    break
            if found:
                break

        processed = set()
        cells_analyze = {start}
        while cells_analyze:
            curr = cells_analyze.pop()
            processed.add(curr)
            neighbours = get_neighbours(curr[0], curr[1], size_x, size_y)
            result += 4 - len(neighbours)
            for neigh in neighbours:
                if grid[neigh[0]][neigh[1]] == 0:
                    result += 1
                elif neigh not in processed:
                    cells_analyze.add(neigh)
        return result


class TestSolution(unittest.TestCase):
    def test_islandPerimeter(self):
        solution = Solution()
        self.assertEqual(16, solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
        self.assertEqual(4, solution.islandPerimeter([[1]]))
        self.assertEqual(4, solution.islandPerimeter([[1, 0]]))
        self.assertEqual(8, solution.islandPerimeter([[1, 1], [1, 1]]))
