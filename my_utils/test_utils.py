import unittest
from my_utils.utils import *


class TestUtils(unittest.TestCase):
    def test_get_neighbours(self):
        result1 = get_neighbours(0, 0, 4, 4)
        self.assertEqual([(0, 1), (1, 0)], result1)

        result2 = get_neighbours(2, 2, 4, 4)
        self.assertEqual([(2, 1), (2, 3), (1, 2), (3, 2)], result2)

        result3 = get_neighbours(2, 2, 3, 4)
        self.assertEqual([(2, 1), (2, 3), (1, 2)], result3)
