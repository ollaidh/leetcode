# Given the root of a binary tree, invert the tree, and return its root.


import unittest
import my_utils.trees as trs


class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        hlp = root.left
        root.left = root.right
        root.right = hlp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class TestInvertTree(unittest.TestCase):
    def test_invertTree(self):
        solution = Solution()
        self.assertEqual(solution.invertTree(trs.create_binary_tree([4, 2, 7, 1, 3, 6, 9])),
                         trs.create_binary_tree([4, 7, 2, 9, 6, 3, 1]))
        self.assertEqual(solution.invertTree(trs.create_binary_tree([2, 1, 3])),
                         trs.create_binary_tree([2, 3, 1]))
        self.assertEqual(solution.invertTree(trs.create_binary_tree([1])),
                         trs.create_binary_tree([1]))
        self.assertEqual(solution.invertTree(trs.create_binary_tree([])),
                         trs.create_binary_tree([]))


if __name__ == '__main__':
    unittest.main()