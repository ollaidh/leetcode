# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


import my_utils.linked_list as lst
import my_utils.testing as test


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = lst.ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


if __name__ == '__main__':
    rev_list = Solution()

    test.run_test(rev_list.mergeTwoLists, (lst.create_linked_list([1, 2, 4, 7]), lst.create_linked_list([1, 3, 4])), lst.create_linked_list([1, 1, 2, 3, 4, 4, 7]), '')
    test.run_test(rev_list.mergeTwoLists, (lst.create_linked_list([5, 5]), lst.create_linked_list([5, 5])), lst.create_linked_list([5, 5, 5, 5]), '')
    test.run_test(rev_list.mergeTwoLists, (lst.create_linked_list([5, 8, 10]), lst.create_linked_list([6, 9, 11, 16, 23, 44])), lst.create_linked_list([5, 6, 8, 9, 10, 11, 16, 23, 44]), '')