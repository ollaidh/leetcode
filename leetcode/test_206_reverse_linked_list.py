# Given the head of a singly linked list, reverse the list,
# and return the reversed list.


import unittest
from typing import Optional
from my_utils.linked_list import *


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


class TestSolution(unittest.TestCase):
    def test_reverseList(self):
        solution = Solution()

        input1 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
        expected1 = create_linked_list([7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(expected1, solution.reverseList(input1))

        input2 = create_linked_list([1, 2, 3, 4])
        expected2 = create_linked_list([4, 3, 2, 1])
        self.assertEqual(expected2, solution.reverseList(input2))

        input3 = create_linked_list([1, 2])
        expected3 = create_linked_list([2, 1])
        self.assertEqual(expected3, solution.reverseList(input3))

        input4 = create_linked_list([1])
        expected4 = create_linked_list([1])
        self.assertEqual(expected4, solution.reverseList(input4))

        input5 = create_linked_list([])
        expected5 = create_linked_list([])
        self.assertEqual(expected5, solution.reverseList(input5))
