# Given the root of a binary tree, invert the tree, and return its root.


import unittest
from typing import Optional

from my_utils.trees import *


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class TestSolution(unittest.TestCase):
    def test_invertTree(self):
        solution = Solution()

        input1 = create_binary_tree([4, 2, 7, 1, 3, 6, 9])
        expected1 = create_binary_tree([4, 7, 2, 9, 6, 3, 1])
        self.assertEqual(expected1, solution.invertTree(input1))

        input2 = create_binary_tree([2, 1, 3])
        expected2 = create_binary_tree([2, 3, 1])
        self.assertEqual(expected2, solution.invertTree(input2))

        input3 = create_binary_tree([])
        expected3 = create_binary_tree([])
        self.assertEqual(expected3, solution.invertTree(input3))
