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
    def reverseList(self, head):
        prev, curr = None, head

        while curr:  # while have not reached the end of linked-list
            tmp = curr.next  # temporary variable to store the values after breaking links
            curr.next = prev  # changing link of curr from curr.next to prev (reversing it from right to left)
            prev = curr  # moving prev to curr (to the right)
            curr = tmp  # moving curr to previous curr.next (to the right)

        return prev


if __name__ == '__main__':
    input_list = create_linked_list([1, 2, 3, 4, 5])
    rev_list = Solution()
    print(rev_list.reverseList(input_list))
