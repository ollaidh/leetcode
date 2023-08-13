# Given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).


import unittest


class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [n for n in str(num)]
        for i in range(len(nums)):
            if nums[i] == '6':
                nums[i] = '9'
                break
        return int(''.join(nums))


class TestMax69(unittest.TestCase):
    def test_maximum69Number(self):
        solution = Solution()
        self.assertEqual(9996, solution.maximum69Number(6996))
        self.assertEqual(9966, solution.maximum69Number(9666))
        self.assertEqual(9999, solution.maximum69Number(9996))
        self.assertEqual(9999, solution.maximum69Number(9999))


if __name__ == '__main__':
    unittest.main()
