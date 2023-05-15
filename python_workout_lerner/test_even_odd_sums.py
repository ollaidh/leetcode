import unittest


def even_odd_sums(seq: list | tuple) -> list:
    sums = []
    evens = seq[0:-1:2]
    odds = seq[1::2]
    sums.append(sum(evens))
    sums.append(sum(odds))
    return sums


def plus_minus(seq: list | tuple) -> int:
    minus = - sum(seq[2:-1:2])
    plus = seq[0] + sum(seq[1::2])
    return plus + minus


class TestEvenOddSum(unittest.TestCase):
    def test_even_odd_sums(self):
        self.assertEqual([90, 120], even_odd_sums([10, 20, 30, 40, 50, 60]))
        self.assertEqual([90, 120], even_odd_sums((10, 20, 30, 40, 50, 60)))

    def test_plus_minus(self):
        self.assertEqual(50, plus_minus([10, 20, 30, 40, 50, 60]))


if __name__ == '__main__':
    unittest.main()
