# Given an integer num, repeatedly add all its digits
# until the result has only one digit, and return it.


import unittest


def sum_digits(n: int) -> int:
    summ = 0
    while n != 0:
        summ += n % 10
        n = n // 10
    return summ


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum_digits(num)
        return num


class TestSolution(unittest.TestCase):
    def test_sum_digits(self):
        self.assertEqual(12, sum_digits(138))
        self.assertEqual(1, sum_digits(1))
        self.assertEqual(1, sum_digits(100))

    def test_addDigits(self):
        solution = Solution()
        self.assertEqual(2, solution.addDigits(38))
        self.assertEqual(0, solution.addDigits(0))
