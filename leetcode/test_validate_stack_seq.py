import unittest


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        pop_ind = 0
        for push in pushed:
            stack.append(push)
            while stack and pop_ind < len(popped) and stack[-1] == popped[pop_ind]:
                stack.pop()
                pop_ind += 1
        return not stack


class TestValidator(unittest.TestCase):
    def test_validateStackSequences(self):
        solution = Solution()
        self.assertTrue(solution.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
        self.assertFalse(solution.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))


if __name__ == '__main__':
    unittest.main()
