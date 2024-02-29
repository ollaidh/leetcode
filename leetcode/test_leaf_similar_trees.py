# Consider all the leaves of a binary tree, from left to right order,
# the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


import unittest
from my_utils import trees as trs


class Solution:
    def calc_leaves(self, root):
        # print(root.val)
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return self.calc_leaves(root.left) + self.calc_leaves(root.right)

    def leafSimilar(self, root1, root2) -> bool:
        return self.calc_leaves(root1) == self.calc_leaves(root2)


class TestLeafSimilar(unittest.TestCase):
    def test_leafSimilar(self):
        solution = Solution()
        # self.assertEqual(solution.leafSimilar(trs.create_binary_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
        #                                       trs.create_binary_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])),True)
        self.assertEqual(solution.leafSimilar(trs.create_binary_tree([1, 2, 3]),
                                              trs.create_binary_tree([1, 3, 2])), False)
        self.assertEqual(solution.leafSimilar(trs.create_binary_tree([1, 2]),
                                              trs.create_binary_tree([2, 2])), True)


if __name__ == '__main__':
    unittest.main()
