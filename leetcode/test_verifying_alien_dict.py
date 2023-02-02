"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true
if and only if the given words are sorted lexicographically in this alien language.
"""
import unittest


class Solution(object):
    def createOrders(self, order: str) -> dict:
        return {order[i]: i for i in range(len(order))}

    def isAlphabetic(self, word1: str, word2: str, orders: dict):
        for i in range(len(word1)):
            try:
                if orders[word1[i]] > orders[word2[i]]:
                    return False
                if orders[word1[i]] < orders[word2[i]]:
                    return True
            except IndexError:
                return False
        return True

    def isAlienSorted(self, words: list[str], order: str):
        orders = self.createOrders(order)
        for i in range(len(words) - 1):
            if not self.isAlphabetic(words[i], words[i + 1], orders):
                return False
        return True


class TestAlienSort(unittest.TestCase):
    def test_createOrders(self):
        solution = Solution()
        self.assertEqual(solution.createOrders("abcde"), {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4})

    def test_isAlphabetic(self):
        solution = Solution()
        self.assertTrue(solution.isAlphabetic("hello", "leetcode", solution.createOrders("hlabcdefgijkmnopqrstuvwxyz")))
        self.assertFalse(solution.isAlphabetic("apple", "app", solution.createOrders("abcdefghijklmnopqrstuvwxyz")))
        self.assertTrue(solution.isAlphabetic("app", "app", solution.createOrders("abcdefghijklmnopqrstuvwxyz")))
        self.assertTrue(solution.isAlphabetic("app", "apple", solution.createOrders("abcdefghijklmnopqrstuvwxyz")))

    def test_isAlienSorted(self):
        solution = Solution()
        self.assertTrue(solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
        self.assertFalse(solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
        self.assertFalse(solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))


if __name__ == '__main__':
    unittest.main()
