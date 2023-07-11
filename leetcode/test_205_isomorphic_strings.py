import unittest


class Solution:
    def isIsomorphic(self, lhs: str, rhs: str) -> bool:
        relations_lhs = {}
        relations_rhs = {}

        for left, right in zip(lhs, rhs):
            if left not in relations_lhs:
                relations_lhs[left] = right
            if right not in relations_rhs:
                relations_rhs[right] = left
            if relations_lhs[left] != right:
                return False
            if relations_rhs[right] != left:
                return False
        return True


class TestIsomorphic(unittest.TestCase):
    def test_isIsomorphic(self):
        solution = Solution()
        self.assertEqual(True, solution.isIsomorphic("foo", "zaa"))
        self.assertEqual(True, solution.isIsomorphic("qwerty", "asdfgh"))
        self.assertEqual(True, solution.isIsomorphic("fozo", "zara"))
        self.assertEqual(False, solution.isIsomorphic("ooops", "spooo"))
        self.assertEqual(False, solution.isIsomorphic("ywerty", "asdfgh"))
        self.assertEqual(False, solution.isIsomorphic("badc", "baba"))
        self.assertEqual(True, solution.isIsomorphic("paper", "title"))
        self.assertEqual(True, solution.isIsomorphic("q", "q"))
        self.assertEqual(True, solution.isIsomorphic("q", "c"))


if __name__ == '__main__':
    unittest.main()
