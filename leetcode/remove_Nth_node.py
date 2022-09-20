# Given the head of a linked list,
# remove the nth node from the end of the list and return its head.

import my_utils.linked_list as lst
import my_utils.testing as tst


class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next is None:
            return None

        mp, np = head, head

        for i in range(n):
            np = np.next

        if np is None:
            return head.next

        while np.next:
            mp = mp.next
            np = np.next
        mp.next = mp.next.next

        return head


if __name__ == '__main__':
    solution = Solution()

    tst.run_test(solution.removeNthFromEnd, (lst.create_linked_list([1, 2, 3, 4, 5]), 2),
                 lst.create_linked_list([1, 2, 3, 5]), '')
    tst.run_test(solution.removeNthFromEnd, (lst.create_linked_list([1, 2]), 1),
                 lst.create_linked_list([1]), '')
    tst.run_test(solution.removeNthFromEnd, (lst.create_linked_list([1, 2]), 2),
                 lst.create_linked_list([2]), '')
    tst.run_test(solution.removeNthFromEnd, (lst.create_linked_list([1]), 1),
                 lst.create_linked_list([]), '')
