import unittest


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_branches(root, index, values):
    if index >= len(values) or values[index] is None:
        return
    root.val = values[index]
    root.left = TreeNode()
    root.right = TreeNode()
    build_tree_branches(root.left, 2 * index + 1, values)
    build_tree_branches(root.right, 2 * index + 2, values)


def create_binary_tree(values: list[int]) -> TreeNode:
    root = TreeNode()
    build_tree_branches(root, 0, values)

    return root


class TestCreateBinaryTree(unittest.TestCase):
    def test_create_binary_tree(self):
        tree = create_binary_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(tree.val, 10)
        self.assertEqual(tree.left.val, 5)
        self.assertEqual(tree.left.left.val, 3)
        self.assertEqual(tree.left.right.val, 7)
        self.assertEqual(tree.left.left.left.val, 1)
        self.assertEqual(tree.left.left.right.val, None)
        self.assertEqual(tree.left.right.left.val, 6)
        self.assertEqual(tree.left.right.right.val, None)
        self.assertEqual(tree.right.val, 15)
        self.assertEqual(tree.right.left.val, 13)
        self.assertEqual(tree.right.right.val, 18)
        self.assertEqual(tree.right.left.left.val, None)
        self.assertEqual(tree.right.left.right.val, None)
        self.assertEqual(tree.right.right.left.val, None)
        self.assertEqual(tree.right.right.right.val, None)

        tree = create_binary_tree([10, 5, 15, 3, None, 13, 18, 1])
        self.assertEqual(tree.val, 10)
        self.assertEqual(tree.left.val, 5)
        self.assertEqual(tree.left.left.val, 3)
        self.assertEqual(tree.left.right.val, None)
        self.assertEqual(tree.left.left.left.val, 1)
        self.assertEqual(tree.left.left.right.val, None)
        self.assertEqual(tree.right.val, 15)
        self.assertEqual(tree.right.left.val, 13)
        self.assertEqual(tree.right.right.val, 18)
        self.assertEqual(tree.right.left.left.val, None)
        self.assertEqual(tree.right.left.right.val, None)
        self.assertEqual(tree.right.right.left.val, None)
        self.assertEqual(tree.right.right.right.val, None)

        tree = create_binary_tree([10, None, 15, None, None, 13, 18])
        self.assertEqual(tree.val, 10)
        self.assertEqual(tree.left.val, None)
        self.assertEqual(tree.right.right.val, 18)
        self.assertEqual(tree.right.val, 15)
        self.assertEqual(tree.right.left.val, 13)
        self.assertEqual(tree.right.right.val, 18)

        tree = create_binary_tree([])
        self.assertEqual(tree.val, None)


if __name__ == '__main__':
    unittest.main()








