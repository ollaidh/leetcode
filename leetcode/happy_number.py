# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in
# a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


import my_utils.testing as tst


class Solution(object):
    def number_to_list(self, number):
        digits = []
        while number != 0:
            digits.append(int(number % 10))
            number = number // 10
        return digits

    def isHappy(self, n):
        seen = set()
        while n != 1:
            digits = self.number_to_list(n)
            n = 0
            for digit in digits:
                n += digit * digit
            if n in seen:
                return False
            seen.add(n)
        return True


if __name__ == '__main__':
    solution = Solution()

    tst.run_test(solution.isHappy, 7, True, '')
    tst.run_test(solution.isHappy, 19, True, '')
    tst.run_test(solution.isHappy, 100, True, '')
    tst.run_test(solution.isHappy, 1111111, True, '')
    tst.run_test(solution.isHappy, 2, False, '')
    tst.run_test(solution.isHappy, 11, False, '')
    tst.run_test(solution.isHappy, 101, False, '')
    tst.run_test(solution.isHappy, 0, False, '')
