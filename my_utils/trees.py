import unittest


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __str__(self):
    #     line = []

    def __eq__(self, other):
        def compare(root1, root2):
            if root1 is not None and root2 is not None:
                if root1.val != root2.val:
                    return False
                if root1.left is None and root1.right is None and root2.left is None and root2.right is None:
                    return True
                return compare(root1.left, root2.left) and compare(root1.right, root2.right)
            if root1 is None and root2 is not None:
                return False
            if root2 is None and root1 is not None:
                return False
            return True

        return compare(self, other)


def build_tree_branches(root, index, values):
    if index >= len(values) or values[index] is None:
        return
    root.val = values[index]
    if 2 * index + 1 < len(values) and values[2 * index + 1] is not None:
        root.left = TreeNode()
    if 2 * index + 2 < len(values) and values[2 * index + 2] is not None:
        root.right = TreeNode()
    build_tree_branches(root.left, 2 * index + 1, values)
    build_tree_branches(root.right, 2 * index + 2, values)


def create_binary_tree(values: list[int]) -> TreeNode:
    if list is None:
        return TreeNode(None)
    root = TreeNode()
    build_tree_branches(root, 0, values)

    return root


if __name__ == '__main__':
    pass








