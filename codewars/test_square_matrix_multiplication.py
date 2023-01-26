# Codewars 'Square Matrix Multiplication' 5 kuy
# Write a function that accepts two square (NxN) matrices (two dimensional arrays),
# and returns the product of the two. Only square matrices will be given.

import unittest
import numpy as np


def matrix_mult(a, b):
    matrix1 = np.array(a)
    matrix2 = np.array(b)
    matrix_result = np.matmul(matrix1, matrix2)
    return [list(line) for line in matrix_result]


class TestMatrMult(unittest.TestCase):
    def test_matrix_mult(self):
        self.assertEqual(matrix_mult([[1, 2], [3, 2]], [[3, 2], [1, 1]]), [[5, 4], [11, 8]])
        self.assertEqual(matrix_mult([[1, 2, 3], [3, 2, 1], [2, 1, 3]], [[4, 5, 6], [6, 5, 4], [4, 6, 5]]),
                         [[28, 33, 29], [28, 31, 31], [26, 33, 31]])


if __name__ == '__main__':
    unittest.main()
