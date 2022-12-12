import unittest
import my_utils.trees as trs


class TestCreateBinaryTree(unittest.TestCase):
    def test_create_binary_tree(self):
        root = trs.create_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(root.val, 10)
        self.assertEqual(root.left.val, 5)
        self.assertEqual(root.left.left.val, 3)
        self.assertEqual(root.left.right.val, 7)
        self.assertEqual(root.left.left.left.val, 1)
        self.assertIsNone(root.left.left.left.left)
        self.assertIsNone(root.left.left.left.right)

        self.assertIsNone(root.left.left.right)
        self.assertEqual(root.left.right.left.val, 6)
        self.assertIsNone(root.left.right.right)
        self.assertEqual(root.right.val, 15)
        self.assertEqual(root.right.left.val, 13)
        self.assertEqual(root.right.right.val, 18)
        self.assertIsNone(root.right.left.left)
        self.assertIsNone(root.right.left.right)
        self.assertIsNone(root.right.right.left)
        self.assertIsNone(root.right.right.right)

        root = trs.create_binary_tree([10, 5, 15, 3, None, 13, 18, 1])
        self.assertEqual(root.val, 10)
        self.assertEqual(root.left.val, 5)
        self.assertEqual(root.left.left.val, 3)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.left.left.left.val, 1)
        self.assertIsNone(root.left.left.right)
        self.assertEqual(root.right.val, 15)
        self.assertEqual(root.right.left.val, 13)
        self.assertEqual(root.right.right.val, 18)
        self.assertIsNone(root.right.left.left)
        self.assertIsNone(root.right.left.right)
        self.assertIsNone(root.right.right.left)
        self.assertIsNone(root.right.right.right)

        root = trs.create_binary_tree([10, None, 15, None, None, 13, 18])
        self.assertEqual(root.val, 10)
        self.assertIsNone(root.left)
        self.assertEqual(root.right.right.val, 18)
        self.assertEqual(root.right.val, 15)
        self.assertEqual(root.right.left.val, 13)
        self.assertEqual(root.right.right.val, 18)

        root = trs.create_binary_tree([])
        print(root)
        self.assertEqual(root.val, None)

    def test_equal_trees(self):
        root1 = trs.create_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        root2 = trs.create_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        root3 = trs.create_binary_tree([10, 5, 15, 3, 7, 13, 20, 1, None, 6])
        root4 = trs.create_binary_tree([10])

        self.assertEqual(root1, root1)
        self.assertEqual(root1, root2)
        self.assertNotEqual(root1, root3)
        self.assertEqual(root4, root4)
        self.assertNotEqual(root3, root4)


if __name__ == '__main__':
    unittest.main()
