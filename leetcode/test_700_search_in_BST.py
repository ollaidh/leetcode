# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return
# the subtree rooted with that node. If such a node does not exist, return null.

import unittest
from typing import Optional
from my_utils.trees import *


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)


class TestSolution(unittest.TestCase):
    def test_searchBST(self):
        solution = Solution()

        input1 = create_binary_tree([4, 2, 7, 1, 3])
        expected1 = create_binary_tree([2, 1, 3])
        self.assertEqual(expected1, solution.searchBST(input1, 2))

        input2 = create_binary_tree([4, 2, 7, 1, 3])
        self.assertEqual(None, solution.searchBST(input2, 5))
