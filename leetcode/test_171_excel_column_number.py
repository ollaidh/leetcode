# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.


import unittest


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = list(columnTitle)
        result = 0
        for i, letter in enumerate(letters):
            digit = ord(letter) - ord('A') + 1
            power = (len(letters) - 1) - i
            result += digit * pow(26, power)
        return result


class TestTTM(unittest.TestCase):
    def test_titleToNumber(self):
        solution = Solution()

        self.assertEqual(3, solution.titleToNumber('C'))
        self.assertEqual(27, solution.titleToNumber('AA'))
        self.assertEqual(28, solution.titleToNumber('AB'))
        self.assertEqual(701, solution.titleToNumber('ZY'))



if __name__ == '__main__':
    unittest.main()
