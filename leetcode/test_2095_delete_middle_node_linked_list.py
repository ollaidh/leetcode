# You are given the head of a linked list. Delete the middle node,
# and return the head of the modified linked list.
#
# The middle node of a linked list of size n is the ⌊n / 2⌋th node
# from the start using 0-based indexing, where ⌊x⌋ denotes the largest
# integer less than or equal to x.


import unittest
from my_utils.linked_list import *
from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head


class TestSolution(unittest.TestCase):
    def test_deleteMiddle(self):
        solution = Solution()

        input1 = create_linked_list([1, 2, 3, 4])
        expected1 = create_linked_list([1, 2, 4])
        self.assertEqual(expected1, solution.deleteMiddle(input1))

        input2 = create_linked_list([1, 2, 3, 4, 5])
        expected2 = create_linked_list([1, 2, 4, 5])
        self.assertEqual(expected2, solution.deleteMiddle(input2))

        input3 = create_linked_list([1, 2])
        expected3 = create_linked_list([1])
        self.assertEqual(expected3, solution.deleteMiddle(input3))

        input4 = create_linked_list([1])
        expected4 = create_linked_list([])
        self.assertEqual(expected4, solution.deleteMiddle(input4))
