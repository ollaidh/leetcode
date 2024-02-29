# A binary tree is named Even-Odd if it meets the following conditions:
# The root of the binary tree is at level index 0, its children are at level index 1,
# their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly
# increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly
# decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.


import unittest
from my_utils.trees import *
from typing import Optional


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        nodes_info = {}

        def is_even_odd_ok(node: TreeNode, curr_level: int) -> bool:
            if node.val is None:
                return True
            if curr_level % 2 == 0 and node.val % 2 != 0:
                return True
            if curr_level % 2 != 0 and node.val % 2 == 0:
                return True
            return False

        def is_asc_desc_ok(node: TreeNode, curr_level: int) -> bool:
            if node is None:
                return True
            # print(curr_level, node.val)
            if curr_level in nodes_info:
                print(nodes_info)
                if nodes_info[curr_level] == node.val:
                    stop = 0
                if curr_level % 2 == 0 and nodes_info[curr_level] < node.val:
                    nodes_info[curr_level] = node.val
                    return True
                if curr_level % 2 != 0 and nodes_info[curr_level] > node.val:
                    nodes_info[curr_level] = node.val
                    return True
                return False
            nodes_info[curr_level] = node.val

            return True

        def check_even_odd(node: TreeNode, curr_level: int) -> bool:
            if node is None:
                return True
            if not is_even_odd_ok(node, curr_level):
                return False
            if not is_asc_desc_ok(node, curr_level):
                return False
            curr_level += 1
            return check_even_odd(node.left, curr_level) and check_even_odd(node.right, curr_level)

        return check_even_odd(root, 0)


class TestSolution(unittest.TestCase):
    def test_isEvenOddTree(self):
        solution = Solution()

        input1 = create_binary_tree_dense([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2])
        self.assertTrue(solution.isEvenOddTree(input1))

        input2 = create_binary_tree_dense([5, 4, 2, 3, 3, 7])
        self.assertFalse(solution.isEvenOddTree(input2))

        input3 = create_binary_tree_dense(
            [13, 34, 32, 23, 25, 27, 29, 44, 40, 36, 34, 30, 30, 28, 26, 3, 7, 9, 11, 15, 17, 21, 25, None, None, 27,
             31, 35, None, 37, None, 30, None, 26, None, None, None, 24, None, 20, 16, 12, 10, None, None, 8, None,
             None, None, None, None, 6, None, None, None, None, None, 15, 19, None, None, None, None, 23, None, 27, 29,
             33, 37, None, None, None, None, None, None, 48, None, None, None, 46, None, None, None, 42, 38, 34, 32,
             None, None, None, None, 19])
        self.assertFalse(solution.isEvenOddTree(input3))
        # assert False
