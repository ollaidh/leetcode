# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

import my_utils.testing as test

class Solution(object):
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def isAlphaNum(self, letter):
        return (ord('A') <= ord(letter) <= ord('Z') or
                ord('a') <= ord(letter) <= ord('z') or
                ord('0') <= ord(letter) <= ord('9'))


if __name__ == '__main__':
    check = Solution()

    test.run_test(check.isPalindrome, 'A man, a plan, a canal: Panama', True)
    test.run_test(check.isPalindrome, 'race a car', False)
    test.run_test(check.isPalindrome, 'FanaRranaf', True)

