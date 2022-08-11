# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.


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
    def deleteDuplicates(self, head):
        if head is None:
            return None
        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == '__main__':
    input_list = create_linked_list([1, 1, 2, 3, 3])
    rev_list = Solution()
    print(rev_list.deleteDuplicates(input_list))