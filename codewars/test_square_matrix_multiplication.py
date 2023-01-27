# Codewars 'Square Matrix Multiplication' 5 kuy
# Write a function that accepts two square (NxN) matrices (two dimensional arrays),
# and returns the product of the two. Only square matrices will be given.

import unittest
import numpy as np
import timeit
import argparse


class UnableMultiplyMatricesError(Exception):
    def __str__(self):
        return "Matrices dimensions do not allow to multiply them. Expected: matrix1 n*m, matrix2 m*n!"


def can_multiply(matrix1, matrix2):
    return matrix1.shape[0] == matrix2.shape[1] and matrix1.shape[1] == matrix2.shape[0]


def matrix_mult_np(a, b):
    matrix1 = np.array(a)
    matrix2 = np.array(b)

    if not can_multiply(matrix1, matrix2):
        raise UnableMultiplyMatricesError

    mult = np.matmul(matrix1, matrix2)
    return mult


def matrix_mult_manual(a, b):
    matrix1 = np.array(a)
    matrix2 = np.array(b)

    if not can_multiply(matrix1, matrix2):
        raise UnableMultiplyMatricesError

    mult = np.full(
        shape=(matrix1.shape[0], matrix2.shape[1]),
        fill_value=0,
        dtype=int
    )

    for i in range(matrix1.shape[0]):
        for j in range(matrix2.shape[1]):
            for k in range(matrix1.shape[1]):
                mult[i, j] += matrix1[i, k] * matrix2[k, j]

    return mult


def matrix_mult(a, b):
    return [list(i) for i in matrix_mult_np(a, b)]


def runtime_compare():
    time_manual = timeit.timeit(
        lambda: matrix_mult_manual([[1, 2, 3], [3, 2, 1], [2, 1, 3]], [[4, 5, 6], [6, 5, 4], [4, 6, 5]]),
        number=100000
    )

    time_np = timeit.timeit(
        lambda: np.matmul([[1, 2, 3], [3, 2, 1], [2, 1, 3]], [[4, 5, 6], [6, 5, 4], [4, 6, 5]]),
        number=100000
    )

    print('Time manual:', time_manual, 'Time using np.matmul:', time_np)


class TestMatricesMult(unittest.TestCase):
    def test_can_multiply(self):
        self.assertTrue(
            can_multiply(
                np.array([[1, 2, 3], [3, 2, 1], [2, 1, 3]]),
                np.array([[4, 5, 6], [6, 5, 4], [4, 6, 5]])
            )
        )
        self.assertTrue(
            can_multiply(
                np.array([[1, 2, 3], [3, 2, 1]]),
                np.array([[4, 5], [6, 5], [4, 6]])
            )
        )
        self.assertFalse(
            can_multiply(
                np.array([[1, 2, 3], [3, 2, 1], [2, 1, 3]]),
                np.array([[6, 5, 4], [4, 6, 5]])
            )
        )

    def test_matrix_mult_manual(self):
        arr1 = np.array([[1, 2], [3, 2]])
        arr2 = np.array([[3, 2], [1, 1]])
        self.assertTrue(
            (matrix_mult_manual(arr1, arr2) == np.matmul(arr1, arr2)).all()
        )

        arr3 = np.array([[1, 2, 3], [3, 2, 1], [2, 1, 3]])
        arr4 = np.array([[4, 5, 6], [6, 5, 4], [4, 6, 5]])
        self.assertTrue(
            (matrix_mult_manual(arr3, arr4) == np.matmul(arr3, arr4)).all()
        )

        arr3 = np.array([[1, 2], [3, 2], [2, 1]])
        arr4 = np.array([[4, 5, 6], [6, 5, 4]])
        self.assertTrue(
            (matrix_mult_manual(arr3, arr4) == np.matmul(arr3, arr4)).all()
        )

        self.assertRaises(UnableMultiplyMatricesError, matrix_mult_np, [[1, 2, 3], [3, 2, 1], [2, 1, 3]],
                          [[6, 5, 4], [4, 6, 5]])

    def test_matrix_mult(self):
        arr1 = np.array([[1, 2], [3, 2]])
        arr2 = np.array([[3, 2], [1, 1]])
        self.assertTrue(
            (matrix_mult_np(arr1, arr2) == np.matmul(arr1, arr2)).all()
        )

        arr3 = np.array([[1, 2, 3], [3, 2, 1], [2, 1, 3]])
        arr4 = np.array([[4, 5, 6], [6, 5, 4], [4, 6666666, 5]])
        self.assertTrue(
            (matrix_mult_np(arr3, arr4) == np.matmul(arr3, arr4)).all()
        )

        arr3 = np.array([[1, 2], [3, 2], [2, 1]])
        arr4 = np.array([[4, 5, 6], [6, 5, 4]])
        self.assertTrue(
            (matrix_mult_np(arr3, arr4) == np.matmul(arr3, arr4)).all()
        )

        self.assertRaises(UnableMultiplyMatricesError, matrix_mult_np, [[1, 2, 3], [3, 2, 1], [2, 1, 3]],
                          [[6, 5, 4], [4, 6, 5]])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--benchmark', action='store_true')
    args = parser.parse_args()

    if args.benchmark:
        runtime_compare()
    else:
        unittest.main()
