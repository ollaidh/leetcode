import my_utils.testing as tst


# defines the ListNode class
class ListNode(object):
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __eq__(self, other):
        head1 = self
        head2 = other
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        if head1 or head2:
            return False
        return True

    def __str__(self):
        line = []
        curr = self
        while curr:  # while have not reached the end of linked-list
            line.append(str(curr.val))
            curr = curr.next
        return '[' + ','.join(line) + ']'


# creates linked list from a regular list. Takes a regular list as input, returns head of linked list
def create_linked_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    curr = head

    for i in range(1, len(lst)):
        curr.next = ListNode(lst[i])
        curr = curr.next

    return head


# creates cycled linked list from a regular list. Takes a regular list as input, returns head of linked list
def create_cycled_linked_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    curr = head

    for i in range(1, len(lst)):
        curr.next = ListNode(lst[i])
        curr = curr.next
    curr.next = head.next.next.next.next.next

    return head


def test_eq():
    tst.verify_if_equal(create_linked_list([0, 1]) == create_linked_list([0, 1]), True, 'Simple test')
    tst.verify_if_equal(create_linked_list([0, 1]) == create_linked_list([1, 2]), False, 'Simple not eq')
    tst.verify_if_equal(create_linked_list([0, 1, 2, 3]) == create_linked_list([0, 1]), False, 'Same beginning')
    tst.verify_if_equal(create_linked_list([0, 1]) == create_linked_list([0, 1, 2, 3]), False, 'Same beginning 2')


if __name__ == '__main__':
    test_eq()
