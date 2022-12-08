import unittest
import my_utils.trees as trs


class TestCreateBinaryTree(unittest.TestCase):
    def test_create_binary_tree(self):
        tree = trs.create_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(tree.val, 10)
        self.assertEqual(tree.left.val, 5)
        self.assertEqual(tree.left.left.val, 3)
        self.assertEqual(tree.left.right.val, 7)
        self.assertEqual(tree.left.left.left.val, 1)
        self.assertIsNone(tree.left.left.left.left)
        self.assertIsNone(tree.left.left.left.right)

        self.assertIsNone(tree.left.left.right)
        self.assertEqual(tree.left.right.left.val, 6)
        self.assertIsNone(tree.left.right.right)
        self.assertEqual(tree.right.val, 15)
        self.assertEqual(tree.right.left.val, 13)
        self.assertEqual(tree.right.right.val, 18)
        self.assertIsNone(tree.right.left.left)
        self.assertIsNone(tree.right.left.right)
        self.assertIsNone(tree.right.right.left)
        self.assertIsNone(tree.right.right.right)

        tree = trs.create_binary_tree([10, 5, 15, 3, None, 13, 18, 1])
        self.assertEqual(tree.val, 10)
        self.assertEqual(tree.left.val, 5)
        self.assertEqual(tree.left.left.val, 3)
        self.assertIsNone(tree.left.right)
        self.assertEqual(tree.left.left.left.val, 1)
        self.assertIsNone(tree.left.left.right)
        self.assertEqual(tree.right.val, 15)
        self.assertEqual(tree.right.left.val, 13)
        self.assertEqual(tree.right.right.val, 18)
        self.assertIsNone(tree.right.left.left)
        self.assertIsNone(tree.right.left.right)
        self.assertIsNone(tree.right.right.left)
        self.assertIsNone(tree.right.right.right)

        tree = trs.create_binary_tree([10, None, 15, None, None, 13, 18])
        self.assertEqual(tree.val, 10)
        self.assertIsNone(tree.left)
        self.assertEqual(tree.right.right.val, 18)
        self.assertEqual(tree.right.val, 15)
        self.assertEqual(tree.right.left.val, 13)
        self.assertEqual(tree.right.right.val, 18)

        tree = trs.create_binary_tree([])
        self.assertIsNone(tree.val)


if __name__ == '__main__':
    unittest.main()
