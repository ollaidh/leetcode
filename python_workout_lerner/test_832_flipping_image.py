# Given an n x n binary matrix image, flip the image horizontally, then invert it,
# and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.


import unittest


class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            lp = 0
            rp = len(image[i]) - 1
            while lp <= rp:
                image[i][lp], image[i][rp] = image[i][rp], image[i][lp]
                lp += 1
                rp -= 1
            for j in range(len(image[i])):
                image[i][j] = 1 - image[i][j]

        return image


class TestSolution(unittest.TestCase):
    def test_flipAndInvertImage(self):
        solution = Solution()
        self.assertEqual([[1, 0, 0], [0, 1, 0], [1, 1, 1]],
                         solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
        self.assertEqual([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]],
                         solution.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
