import my_utils.testing as tst
import my_utils.linked_list as lst


class Solution(object):
    def find_middle_node(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_linked_list(self, head):
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
        return new_head

    def isPalindrome(self, head):
        middle_node = self.find_middle_node(head)
        reversed_half_list = self.reverse_linked_list(middle_node)
        while head and reversed_half_list:
            if head.val != reversed_half_list.val:
                return False
            else:
                head = head.next
                reversed_half_list = reversed_half_list.next
        return True


if __name__ == '__main__':
    solution = Solution()
    tst.run_test(solution.isPalindrome, lst.create_linked_list([1, 2, 2, 1]), True)
    tst.run_test(solution.isPalindrome, lst.create_linked_list([1, 2, 3, 5, 3, 2, 1]), True)
    tst.run_test(solution.isPalindrome, lst.create_linked_list([1, 2]), False)
    tst.run_test(solution.isPalindrome, lst.create_linked_list([1]), True)
    tst.run_test(solution.isPalindrome, lst.create_linked_list([]), True)

