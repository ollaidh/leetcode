# You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.)
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return 0.


import unittest
from my_utils.utils import get_neighbours


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        result = 0

        size_x = len(grid)
        size_y = len(grid[0])

        processed = set()

        for i in range(size_x):
            for j in range(size_y):
                if grid[i][j] == 1 and (i, j) not in processed:
                    area = 1
                    cells_analyze = {(i, j)}
                    processed.add((i, j))
                    while cells_analyze:
                        curr = cells_analyze.pop()
                        neighbours = get_neighbours(curr[0], curr[1], size_x, size_y)
                        for neigh in neighbours:
                            if grid[neigh[0]][neigh[1]] == 1 and neigh not in processed:
                                area += 1
                                cells_analyze.add(neigh)
                                processed.add(neigh)
                    result = max(result, area)
        return result


class TestSolution(unittest.TestCase):
    def test_maxAreaOfIsland(self):
        solution = Solution()
        self.assertEqual(6, solution.maxAreaOfIsland(
            [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
        self.assertEqual(0, solution.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
        self.assertEqual(4, solution.maxAreaOfIsland(
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1]
            ]
        ))
