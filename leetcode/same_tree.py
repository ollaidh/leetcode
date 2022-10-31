# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


import my_utils.testing as tst
import my_utils.trees as btr


class Solution(object):
    def isSameTree(self, p, q):

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    solution = Solution()
    tst.run_test(solution.isSameTree, (btr.create_binary_tree([1, 2, 3]), btr.create_binary_tree([1, 2, 3])), True, '')
    tst.run_test(solution.isSameTree, (btr.create_binary_tree([1, 2]), btr.create_binary_tree([1, None, 3])), False, '')
    tst.run_test(solution.isSameTree, (btr.create_binary_tree([]), btr.create_binary_tree([])), True, '')
    tst.run_test(solution.isSameTree, (btr.create_binary_tree([1, 2, 1]), btr.create_binary_tree([1, 1, 2])), False, '')
    tst.run_test(solution.isSameTree, (btr.create_binary_tree([]), btr.create_binary_tree([0])), False, '')
    tst.run_test(solution.isSameTree, (btr.create_binary_tree([10, 5, 15]), btr.create_binary_tree([10, 5, None, None,
                                                                                                    15])), False, '')

