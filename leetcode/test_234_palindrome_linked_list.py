# Given the head of a singly linked list,
# return true if it is a palindrome or false otherwise.


import unittest
from typing import Optional

from my_utils.linked_list import *


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:
            print(prev.val, head.val)
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True


class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        solution = Solution()

        input1 = create_linked_list([1, 2, 3, 2, 1])
        self.assertTrue(solution.isPalindrome(input1))

        input2 = create_linked_list([1, 2, 3, 3, 2, 1])
        self.assertTrue(solution.isPalindrome(input2))

        input3 = create_linked_list([1, 2, 3, 2, 2, 1])
        self.assertFalse(solution.isPalindrome(input3))

        input4 = create_linked_list([1, 1])
        self.assertTrue(solution.isPalindrome(input4))

        input5 = create_linked_list([1, 2])
        self.assertFalse(solution.isPalindrome(input5))

        input6 = create_linked_list([1])
        self.assertTrue(solution.isPalindrome(input6))

        input6 = create_linked_list([])
        self.assertTrue(solution.isPalindrome(input6))

        input7 = create_linked_list([1, 2, 2, 1])
        self.assertTrue(solution.isPalindrome(input7))
