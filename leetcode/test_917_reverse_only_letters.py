# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.


import unittest


def is_letter(symbol:str) -> bool:
    return 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        symbols = list(s)
        lp = 0
        rp = len(s) - 1
        while lp <= rp:
            if is_letter(symbols[lp]) and is_letter(symbols[rp]):
                symbols[lp], symbols[rp] = symbols[rp], symbols[lp]
                lp += 1
                rp -= 1
            else:
                if not is_letter(symbols[lp]):
                    lp += 1
                if not is_letter(symbols[rp]):
                    rp -= 1
        return "".join(symbols)


class TestSolution(unittest.TestCase):
    def test_is_letter(self):
        self.assertTrue(is_letter("a"))
        self.assertTrue(is_letter("d"))
        self.assertTrue(is_letter("G"))
        self.assertTrue(is_letter("Z"))
        self.assertFalse(is_letter("-"))
        self.assertFalse(is_letter("&"))
        self.assertFalse(is_letter("^"))

    def test_reverseOnlyLetters(self):
        solution = Solution()
        self.assertEqual("dc-ba", solution.reverseOnlyLetters("ab-cd"))
        self.assertEqual("j-Ih-gfE-dCba", solution.reverseOnlyLetters("a-bC-dEf-ghIj"))
        self.assertEqual("Qedo1ct-eeLg=ntse-T!", solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
