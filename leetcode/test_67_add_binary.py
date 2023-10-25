# Given two binary strings a and b, return their sum as a binary string.


import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summ = []
        add = 0
        if len(b) > len(a):
            a, b = b, a

        for i in range(len(a) - 1, -1, -1):
            if i - (len(a) - len(b)) >= 0:
                curr_sum = int(a[i]) + int(b[i - (len(a) - len(b))]) + add
            else:
                curr_sum = int(a[i]) + add
            if curr_sum == 3:
                summ.append("1")
                add = 1
            elif curr_sum == 2:
                summ.append("0")
                add = 1
            else:
                summ.append(str(curr_sum))
                add = 0
        if add == 1:
            summ.append("1")

        return "".join(summ[::-1])


class TestSolution(unittest.TestCase):
    def test_addBinary(self):
        solution = Solution()
        self.assertEqual("100", solution.addBinary("11", "1"))
        self.assertEqual("10101", solution.addBinary("1010", "1011"))
