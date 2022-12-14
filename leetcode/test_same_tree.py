# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


import unittest
import my_utils.trees as trs


class Solution:
    def isSameTree(self, p, q) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class TestSameTree(unittest.TestCase):
    def test_isSameTree(self):
        solution = Solution()
        self.assertEqual(solution.isSameTree(trs.create_binary_tree([1, 2, 3]), trs.create_binary_tree([1, 2, 3])),
                         True)
        self.assertEqual(solution.isSameTree(trs.create_binary_tree([1, 2]), trs.create_binary_tree([1, None, 2])),
                         False)
        self.assertEqual(solution.isSameTree(trs.create_binary_tree([1, 2, 1]), trs.create_binary_tree([1, 1, 2])),
                         False)
        self.assertEqual(solution.isSameTree(trs.create_binary_tree([]), trs.create_binary_tree([])),
                         True)


if __name__ == '__main__':
    unittest.main()
