# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].


import unittest
import my_utils.trees as trs


class Solution:
    def rangeSumBST(self, root, low: int, high: int):
        if root is None or root.val is None:
            return 0
        if low <= root.val <= high:
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + root.val
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        else:
            return self.rangeSumBST(root.left, low, high)


class TestRangeSumBST(unittest.TestCase):
    def test_rangeSumBST(self):
        solution = Solution()

        self.assertEqual(solution.rangeSumBST(trs.create_binary_tree([10, 5, 15, 3, 7, None, 18]), 7, 15), 32)
        self.assertEqual(solution.rangeSumBST(trs.create_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10), 23)
        self.assertEqual(solution.rangeSumBST(trs.create_binary_tree([]), 6, 10), 0)


if __name__ == '__main__':
    unittest.main()
