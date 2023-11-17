import unittest


def sum_recursive(sequence: list[int]) -> int:
    if not sequence:
        return 0
    if len(sequence) == 1:
        return sequence[0]
    return sequence[0] + sum_recursive(sequence[1:])


def sort_recursive(sequence: list[int]) -> list[int]:
    if len(sequence) <= 1:
        return sequence
    ind = len(sequence) // 2
    less = []
    more = []
    mid = []
    for num in sequence:
        if num < sequence[ind]:
            less.append(num)
        elif num > sequence[ind]:
            more.append(num)
        else:
            mid.append(num)
    return sort_recursive(less) + mid + sort_recursive(more)


class TestRecursions(unittest.TestCase):
    def test_sum_recursive(self):
        self.assertEqual(10, sum_recursive([1, 2, 4, 2, 1, 0]))
        self.assertEqual(10, sum_recursive([10]))
        self.assertEqual(0, sum_recursive([]))

    def test_sort_recursive(self):
        self.assertEqual([1, 2, 3, 4, 5], sort_recursive([5, 3, 4, 1, 2]))
        self.assertEqual([1, 2], sort_recursive([2, 1]))
        self.assertEqual([1, 2], sort_recursive([1, 2]))
        self.assertEqual([1, 1], sort_recursive([1, 1]))
        self.assertEqual([1], sort_recursive([1]))
