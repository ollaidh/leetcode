# Given the heads of two singly linked-lists headA and headB,
# return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null

import my_utils.testing as tst
import my_utils.linked_list as lst


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        nodes_seen = set()
        currA = headA
        currB = headB

        while currA:
            nodes_seen.add(currA)
            currA = currA.next

        while currB:
            if currB in nodes_seen:
                return currB
            currB = currB.next

        return None


if __name__ == '__main__':
    headA, headB, inter_node = lst.create_two_intersected_lists([1, 2, 4], [8, 1, 6, 2], [100, 1, 5, 2])

    solution = Solution()
    tst.run_test(solution.getIntersectionNode, (headA, headB), inter_node, '')
