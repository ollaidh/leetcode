# Given a roman numeral, convert it to an integer.


import unittest


class Solution(object):
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        added = 0

        for i in range(len(s) - 1, -1, -1):
            current = roman[s[i]]
            if current >= added:
                result += current
                added = current
            else:
                result -= current

        return result


class TestRTI(unittest.TestCase):
    def test_romanToInt(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('III'), 3)
        self.assertEqual(solution.romanToInt('IX'), 9)
        self.assertEqual(solution.romanToInt('XI'), 11)
        self.assertEqual(solution.romanToInt('XIV'), 14)
        self.assertEqual(solution.romanToInt('LVIII'), 58)
        self.assertEqual(solution.romanToInt('MCMXCIV'), 1994)


if __name__ == '__main__':
    unittest.main()
