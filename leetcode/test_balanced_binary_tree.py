# Given a binary tree, determine if it is Height-Balanced
# A height-balanced binary tree is a binary tree in which
# the depth of the two subtrees of every node never differs by more than one.


import unittest
import my_utils.trees as trs


class Solution:
    def isBalanced(self, root) -> bool:
        def maxDepth(root) -> int:
            if root is None or root.val is None:
                return 0
            return max(maxDepth(root.left), maxDepth(root.right)) + 1

        def calc(root):
            if root is None:
                return True
            if abs(maxDepth(root.left) - maxDepth(root.right)) > 1:
                return False
            return calc(root.left) and calc(root.right)

        return calc(root)


class TestBalanced(unittest.TestCase):
    def test_isBalanced(self):
        solution = Solution()
        self.assertEqual(solution.isBalanced(trs.create_binary_tree([3, 9, 20, None, None, 15, 7])), True)
        self.assertEqual(solution.isBalanced(trs.create_binary_tree([1, 2, 7, 3, 5, None, None, 4, 6])), False)
        self.assertEqual(solution.isBalanced(trs.create_binary_tree([])), True)
        self.assertEqual(solution.isBalanced(trs.create_binary_tree([1])), True)


if __name__ == '__main__':
    unittest.main()
