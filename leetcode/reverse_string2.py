# Given a string s and an integer k, reverse the first k characters
# for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them.
# If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and leave the other as original.

import my_utils.testing as tst


class Solution(object):
    def reverseStr(self, s, k):
        if not s:
            return ''

        if k > len(s):
            k = len(s)

        word = [letter for letter in s]
        lp, rp = 0, k - 1

        while lp < len(s):
            ilp, irp = lp, rp
            while ilp < irp:
                word[ilp], word[irp] = word[irp], word[ilp]
                ilp += 1
                irp -= 1
            lp = lp + 2 * k
            rp = min(rp + 2 * k, len(s) - 1)

        return ''.join(word)


if __name__ == '__main__':
    solution = Solution()
    tst.run_test(solution.reverseStr, ('abcdefg', 2), 'bacdfeg', '')
    tst.run_test(solution.reverseStr, ('abcd', 2), 'bacd', '')
    tst.run_test(solution.reverseStr, ('abc', 4), 'cba', '')
    tst.run_test(solution.reverseStr, ('a', 1), 'a', '')
    tst.run_test(solution.reverseStr, ('', 4), '', '')
    tst.run_test(solution.reverseStr, ('hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl', 39), 'fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi', '')
