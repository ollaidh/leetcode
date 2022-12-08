import unittest
from my_utils import trees as trs


class SumBST:
    def sum_bst_nodes(self, root):
        if root is None or root.val is None:
            return 0
        return self.sum_bst_nodes(root.left) + self.sum_bst_nodes(root.right) + root.val


class TestSumBst(unittest.TestCase):
    def test_sum_bst_nodes(self):
        solution = SumBST()
        self.assertEqual(solution.sum_bst_nodes(trs.create_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])), 78)
        self.assertEqual(solution.sum_bst_nodes(trs.create_binary_tree([10, 5, 15, 3, 7, None, 18])), 58)
        self.assertEqual(solution.sum_bst_nodes(trs.create_binary_tree([])), 0)


if __name__ == '__main__':
    unittest.main()
