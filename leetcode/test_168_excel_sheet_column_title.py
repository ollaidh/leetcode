# Given an integer columnNumber, return its corresponding column title
# as it appears in an Excel sheet.


import unittest


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        start = ord("A")
        result = []
        while columnNumber > 0:
            result.append(chr(start + (columnNumber - 1) % 26))
            columnNumber = (columnNumber - 1) // 26
        return "".join(result[::-1])


class TestSolution(unittest.TestCase):
    def test_convertToTitle(self):
        solution = Solution()
        self.assertEqual("A", solution.convertToTitle(1))
        self.assertEqual("Z", solution.convertToTitle(26))
        self.assertEqual("AB", solution.convertToTitle(28))
        self.assertEqual("AZ", solution.convertToTitle(52))
        self.assertEqual("ZY", solution.convertToTitle(701))
