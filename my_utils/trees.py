import my_utils.testing as tst

# defines a TreeNode class


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        line = []
        curr = self
        line.append(str(curr.val))
        while True:  # while have not reached the end of binary tree
            while True:
                if curr.left:
                    curr = curr.left
                    line.append(str(curr.val))
                else:
                    #line.append('None')
                    break
            if curr.right:
                line.append('None')
                curr = curr.right
                line.append(str(curr.val))
            else:
                break

        return '[' + ','.join(line) + ']'


def create_binary_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    curr = root
    curr_ind = 1

    while curr_ind < len(lst):
        while curr_ind < len(lst) and lst[curr_ind]:
            curr.left = TreeNode(lst[curr_ind])
            curr = curr.left
            curr_ind += 1
        curr_ind += 1
        if curr_ind < len(lst):
            curr.right = TreeNode(lst[curr_ind])
            curr = curr.right
            curr_ind += 1

    return root


def test_print_binary_tree():
    tst.verify_if_equal(str(create_binary_tree([1, None, 2, 3])) == '[1,None,2,3]', True, '')
    tst.verify_if_equal(str(create_binary_tree([1, 4, None, 2, 3])) == '[1,4,None,2,3]', True, '')


if __name__ == '__main__':
    test_print_binary_tree()
