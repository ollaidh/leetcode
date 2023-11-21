# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color.
# You should perform a flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels connected
# 4-directionally to the starting pixel of the same color as the starting pixel,
# plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
# Replace the color of all of the aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.


import unittest

from my_utils.utils import get_neighbours


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        base_color = image[sr][sc]

        if base_color == color:
            return image

        cells_to_analyze = [(sr, sc)]
        size_x = len(image)
        size_y = len(image[0])
        while cells_to_analyze:
            curr = cells_to_analyze.pop()
            image[curr[0]][curr[1]] = color
            neighbours = get_neighbours(curr[0], curr[1], size_x, size_y)
            for neigh in neighbours:
                if image[neigh[0]][neigh[1]] == base_color:
                    cells_to_analyze.append((neigh[0], neigh[1]))

        return image


class TestSolution(unittest.TestCase):
    def test_floodFill(self):
        solution = Solution()
        self.assertEqual(
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
            solution.floodFill(
                image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2
            )
        )
        self.assertEqual(
            [[0, 0, 0], [0, 0, 0]],
            solution.floodFill(
                image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0
            )
        )
