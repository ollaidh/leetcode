# Given the root of a binary tree, return the inorder traversal of its nodes' values.

import my_utils.testing as tst
import my_utils.trees as btr

class Solution(object):
    def inorderTraversal(self, root):
        tree_stack = []
        traversed_line = []
        curr = root
        while curr or tree_stack:
            while curr:
                tree_stack.append(curr)
                curr = curr.left
            curr = tree_stack.pop()
            traversed_line.append(curr.val)
            curr = curr.right
        return traversed_line


if __name__ == '__main__':
    solution = Solution()
    tst.run_test(solution.inorderTraversal, btr.create_binary_tree([1, None, 2, 3]), [1, 3, 2], '')
    tst.run_test(solution.inorderTraversal, btr.create_binary_tree([]), [], '')
    tst.run_test(solution.inorderTraversal, btr.create_binary_tree([1]), [1], '')
