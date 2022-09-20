# Function that reverses a string.
# The input string is given as an array of characters s.
# Do by modifying the input array in-place with O(1) extra memory.


import my_utils.testing as tst


class Solution(object):
    def reverseString(self, s):
        lp, rp = 0, (len(s) - 1)
        while lp < rp:
            s[lp], s[rp] = s[rp], s[lp]
            rp -= 1
            lp += 1
        return s


if __name__ == '__main__':
    solution = Solution()

    tst.run_test(solution.reverseString, (["h", "e", "l", "l", "o"], ), ["o", "l", "l", "e", "h"], '')
    tst.run_test(solution.reverseString, (["H", "a", "n", "n", "a", "h"], ), ["h", "a", "n", "n", "a", "H"], '')
    tst.run_test(solution.reverseString, (["h", "o"], ), ["o", "h"], '')
    tst.run_test(solution.reverseString, (["X"], ), ["X"], '')
    tst.run_test(solution.reverseString, ([], ), [], '')
