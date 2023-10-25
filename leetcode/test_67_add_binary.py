# Given two binary strings a and b, return their sum as a binary string.


import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summ = []
        add = 0
        if len(b) > len(a):
            a, b = b, a

        for i in range(len(a)):
            first = int(a[-i - 1])
            second = int(b[-i - 1] if i < len(b) else 0)
            curr_sum = first + second + add
            add = 0
            if curr_sum >= 2:
                add = 1
            summ.append(str(curr_sum % 2))

        if add == 1:
            summ.append("1")

        return "".join(summ[::-1])


class TestSolution(unittest.TestCase):
    def test_addBinary(self):
        solution = Solution()
        self.assertEqual("100", solution.addBinary("11", "1"))
        self.assertEqual("10101", solution.addBinary("1010", "1011"))
