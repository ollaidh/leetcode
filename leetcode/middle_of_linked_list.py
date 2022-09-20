# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


import my_utils.testing as tst
import my_utils.linked_list as lst


class Solution(object):
    def middleNode(self, head):
        lp, rp = head, head
        while rp and rp.next:
            lp = lp.next
            rp = rp.next.next
        return lp


if __name__ == '__main__':
    solution = Solution()
    linked_list = lst.create_linked_list([1, 2, 3, 4, 5, 6])

    tst.run_test(solution.middleNode, lst.create_linked_list([]), lst.create_linked_list([]), '')
    tst.run_test(solution.middleNode, lst.create_linked_list([1]), lst.create_linked_list([1]), '')
    tst.run_test(solution.middleNode, lst.create_linked_list([1, 2, 3, 4, 5]), lst.create_linked_list([3, 4, 5]), '')
    tst.run_test(solution.middleNode, lst.create_linked_list([1, 2, 3, 4, 5, 6]), lst.create_linked_list([4, 5, 6]), '')



