# Given an integer x, return true if x is palindrome integer.
# Without converting the integer to a string

import my_utils.testing as tst


class Solution(object):
    def isPalindrome(self, x):
        x_inv = 0
        dummy = x

        if x < 0:
            return False

        while dummy > 0:
            digit = dummy % 10
            x_inv = x_inv * 10 + digit
            dummy = dummy // 10

        return x == x_inv


if __name__ == '__main__':
    solution = Solution()

    tst.run_test(solution.isPalindrome, 12345, False, '')
    tst.run_test(solution.isPalindrome, 123454321, True, '')
    tst.run_test(solution.isPalindrome, -100, False, '')
    tst.run_test(solution.isPalindrome, 121, True, '')
    tst.run_test(solution.isPalindrome, 1001, True, '')

