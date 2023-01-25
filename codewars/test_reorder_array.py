# Codewars 'Reorder Array 2' 6 kuy
# You get two integers N and M. Return an array with two sub-arrays with numbers in ranges [0, N / 2) and [N / 2, N)
# respectively, each of them being rotated M times.


import unittest
import numpy as np


def reorder(a, b):
    arr = np.arange(a).reshape(2, a // 2)
    rolled = [list(np.roll(arr[i], b)) for i in range(2)]
    return rolled


class TestReOrder(unittest.TestCase):
    def test_reoeder(self):
        self.assertEqual(reorder(10, 1), [[4, 0, 1, 2, 3], [9, 5, 6, 7, 8]])
        self.assertEqual(reorder(10, 3), [[2, 3, 4, 0, 1], [7, 8, 9, 5, 6]])
        self.assertEqual(reorder(10, 97), [[3, 4, 0, 1, 2], [8, 9, 5, 6, 7]])


if __name__ == '__main__':
    unittest.main()
