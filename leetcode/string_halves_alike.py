# You are given a string s of even length. Split this string into two halves of equal lengths,
# and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels
# ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.


import unittest


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left_half_counter = 0
        right_half_counter = 0
        vowels = set('aeiouAEIOU')
        for i in range(len(s)):
            if s[i] in vowels:
                if i < (len(s) / 2):
                    left_half_counter += 1
                else:
                    right_half_counter += 1
                    if right_half_counter > left_half_counter:
                        return False
        return left_half_counter == right_half_counter


class TestStrHalfEven(unittest.TestCase):
    def test_halvesAreAlike(self):
        solution = Solution()
        self.assertEqual(solution.halvesAreAlike('book'), True)
        self.assertEqual(solution.halvesAreAlike('fooosa'), True)
        self.assertEqual(solution.halvesAreAlike('gagaga'), False)


if __name__ == '__main__':
    unittest.main()
