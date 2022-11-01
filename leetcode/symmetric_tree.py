# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


import my_utils.trees as btr
import my_utils.testing as tst


class Solution(object):
    def isSymmetric(self, root):
        return self.isMirrored(root, root)


    def isMirrored(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.isMirrored(root1.left, root2.right) and self.isMirrored(root1.right,
                                                                                                       root2.left)


if __name__ == '__main__':
    solution = Solution()
    tst.run_test(solution.isSymmetric, btr.create_binary_tree([1, 2, 2, 3, 4, 4, 3]), True, '')
    tst.run_test(solution.isSymmetric, btr.create_binary_tree([1, 2, 2, None, 3, None, 3]), False, '')
    tst.run_test(solution.isSymmetric, btr.create_binary_tree([]), True, '')
    tst.run_test(solution.isSymmetric, btr.create_binary_tree([1]), True, '')
