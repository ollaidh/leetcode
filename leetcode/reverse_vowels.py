# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u',
# and they can appear in both lower and upper cases, more than once.

import my_utils.testing as tst

class Solution(object):
    def reverseVowels(self, s):
        word = [x for x in s]
        lp, rp = 0, len(word) - 1
        vowels = {'a', 'e', 'i', 'o', 'u',  'A', 'E', 'I', 'O', 'U'}
        while lp < rp:
            while word[lp] not in vowels and lp < rp:
                lp += 1
            while word[rp] not in vowels and lp < rp:
                rp -= 1
            word[lp], word[rp] = word[rp], word[lp]
            lp += 1
            rp -= 1
        return ''.join(word)


if __name__ == '__main__':
    solution = Solution()
    tst.run_test(solution.reverseVowels, 'hello', 'holle', '')
    tst.run_test(solution.reverseVowels, 'leetcode', 'leotcede', '')
    tst.run_test(solution.reverseVowels, '', '', '')
    tst.run_test(solution.reverseVowels, 'a', 'a', '')
    tst.run_test(solution.reverseVowels, 'oa', 'ao', '')
