# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again
# by continuously following the next pointer. Internally, pos is used to denote the index of the node
# that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

import unittest
from my_utils import linked_list as llst


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


class Solution(object):
    # O(n) memory because it uses set.
    def hasCycle(self, head):
        cyclic = set()
        curr = head
        while curr:
            if curr in cyclic:
                return True
            else:
                cyclic.add(curr)
                curr = curr.next
        return False

    # O(1) memory. Solution is bad because it screws the initial data. But it is fast and funny.
    def hasCycleCheat(self, head):
        while head:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False

    # O(1) memory
    def hasCyclePointers(self, head):
        sp = head  # "slow" pointer, moves 1 next per step
        fp = head  # "fast" pointer, moves 2 nexts per step

        while sp and fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            print(fp.val)
            if id(fp) == id(sp):  # slow pointer could "meet" fast pointer only in case if we have a cycle
                return True
        return False


class TestSolution(unittest.TestCase):
    def test_hasCycle(self):
        solution = Solution()

        input1 = llst.create_cycled_linked_list([1, 2, 3, 4, 5], 1)
        self.assertTrue(solution.hasCycle(input1))
        self.assertTrue(solution.hasCycleCheat(input1))
        self.assertTrue(solution.hasCyclePointers(input1))

        input2 = llst.create_cycled_linked_list([3, 2, 0, -4], 2)
        self.assertTrue(solution.hasCycle(input2))
        self.assertTrue(solution.hasCycleCheat(input2))
        self.assertTrue(solution.hasCyclePointers(input2))

        input3 = llst.create_linked_list([1])
        self.assertFalse(solution.hasCycle(input3))
        self.assertFalse(solution.hasCycleCheat(input3))
        self.assertFalse(solution.hasCyclePointers(input3))
