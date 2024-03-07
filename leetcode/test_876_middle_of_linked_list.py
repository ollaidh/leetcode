# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.


import unittest
import my_utils.linked_list as lst


class Solution(object):
    def middleNode(self, head):
        lp, rp = head, head
        while rp and rp.next:
            lp = lp.next
            rp = rp.next.next
        return lp


class TestMiddleMode(unittest.TestCase):
    def test_middleNode(self):
        solution = Solution()
        self.assertEqual(solution.middleNode(lst.create_linked_list([])),
                         lst.create_linked_list([]))
        self.assertEqual(solution.middleNode(lst.create_linked_list([1])),
                         lst.create_linked_list([1]))
        self.assertEqual(solution.middleNode(lst.create_linked_list([1, 2, 3, 4, 5])),
                         lst.create_linked_list([3, 4, 5]))
        self.assertEqual(solution.middleNode(lst.create_linked_list([1, 2, 3, 4, 5, 6])),
                         lst.create_linked_list([4, 5, 6]))


if __name__ == '__main__':
    unittest.main()



