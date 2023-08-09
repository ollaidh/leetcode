# Given a list of strings words and a string pattern, return a list of words[i] that match pattern.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every
# letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
# and no two letters map to the same letter.


import unittest


class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def is_matched(mapping: dict, key: str, value: str) -> bool:
            if key not in mapping:
                mapping[key] = value
            return mapping[key] == value

        def is_word_matched(wrd: str, pttrn: str) -> bool:
            pattern_mapping = {}
            word_mapping = {}
            for pattern_letter, word_letter in zip(pttrn, wrd):
                if (not is_matched(pattern_mapping, pattern_letter, word_letter) or
                        not is_matched(word_mapping, word_letter, pattern_letter)):
                    return False
            return True

        result = []
        for word in words:
            if is_word_matched(word, pattern):
                result.append(word)

        return result


class TestFindReplace(unittest.TestCase):
    def test_findAndReplacePattern(self):
        solution = Solution()
        self.assertEqual(["mee", "aqq"],
                         solution.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
        self.assertEqual(["a", "b", "c"],
                         solution.findAndReplacePattern(["a", "b", "c"], "a"))
        self.assertEqual(["bbb"],
                         solution.findAndReplacePattern(["abb", "bbb", "caa"], "fff"))
        self.assertEqual([],
                         solution.findAndReplacePattern(["abb", "bbb", "caa"], "faf"))


if __name__ == '__main__':
    unittest.main()
