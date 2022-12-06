# Given the head of a singly linked list, group all the nodes
# with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.


import unittest
import my_utils.linked_list as lst


class Solution:
    def oddEvenList(self, head):
        if not head:
            return None

        if not head.next or not head.next.next:
            return head

        head_odd = head
        head_even = head.next

        curr_odd = head_odd
        curr_even = head_even

        head = head.next.next
        while head:
            curr_odd.next = head
            curr_odd = curr_odd.next
            curr_even.next = head.next
            curr_even = curr_even.next
            if not head.next:
                break
            head = head.next.next

        curr_odd.next = head_even
        return head_odd


class TestOddEven(unittest.TestCase):
    def test_oddEvenList(self):
        solution = Solution()
        self.assertEqual(solution.oddEvenList(lst.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])),
                         lst.create_linked_list([1, 3, 5, 7, 2, 4, 6, 8]))
        self.assertEqual(solution.oddEvenList(lst.create_linked_list([1, 2, 3, 4, 5])),
                         lst.create_linked_list([1, 3, 5, 2, 4]))
        self.assertEqual(solution.oddEvenList(lst.create_linked_list([2, 1, 3, 5, 6, 4, 7])),
                         lst.create_linked_list([2, 3, 6, 7, 1, 5, 4]))
        self.assertEqual(solution.oddEvenList(lst.create_linked_list([1, 2])),
                         lst.create_linked_list([1, 2]))
        self.assertEqual(solution.oddEvenList(lst.create_linked_list([])),
                         lst.create_linked_list([]))


if __name__ == '__main__':
    unittest.main()


