# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


class ListNode(object):
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        line = []
        curr = self
        while curr:  # while have not reached the end of linked-list
            line.append(str(curr.val))
            curr = curr.next
        return ' '.join(line)


def create_linked_list(lst):
    head = ListNode(lst[0])
    curr = head

    for i in range(1, len(lst)):
        curr.next = ListNode(lst[i])
        curr = curr.next

    return head


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
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
    input_list1 = create_linked_list([1, 2, 4, 7])
    input_list2 = create_linked_list([1, 3, 4])
    rev_list = Solution()
    print(rev_list.mergeTwoLists(input_list1, input_list2))