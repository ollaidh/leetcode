# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes, insert a new node with a value equal to
# the greatest common divisor of them. Return the linked list after insertion.


import unittest

from typing import Optional

import my_utils.testing as tst
from my_utils import linked_list as lst
from my_utils import create_linked_list


def calc_gcd(a: int, b: int) -> int:
    rem1 = max(a, b) % min(a, b)
    if rem1 == 0:
        return min(a, b)
    rem2 = min(a, b) % rem1
    if rem2 == 0:
        return rem1
    rem3 = rem1 % rem2
    while rem3 > 0:
        rem1 = rem2
        rem2 = rem3
        rem3 = rem1 % rem2
    return rem2


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[lst.ListNode]) -> Optional[lst.ListNode]:
        curr_node = head
        next_node = head.next
        while curr_node and curr_node.next:
            gcd = lst.ListNode(calc_gcd(curr_node.val, next_node.val))
            curr_node.next = gcd
            gcd.next = next_node
            curr_node = next_node
            next_node = curr_node.next

        return head


class TestInsertGCD(unittest.TestCase):
    def test_calc_gcd(self):
        self.assertEqual(4, calc_gcd(140, 96))
        self.assertEqual(6, calc_gcd(84, 90))
        self.assertEqual(9, calc_gcd(27, 9))
        self.assertEqual(1, calc_gcd(15, 28))

    def test_insertGreatestCommonDivisors(self):
        solution = Solution()
        tst.verify_if_equal(
            solution.insertGreatestCommonDivisors(create_linked_list([18, 6, 10, 3])),
            create_linked_list([18, 6, 6, 2, 10, 1, 3]),
            '')
        tst.verify_if_equal(
            solution.insertGreatestCommonDivisors(create_linked_list([7])),
            create_linked_list([7]),
            '')


if __name__ == '__main__':
    unittest.main()
