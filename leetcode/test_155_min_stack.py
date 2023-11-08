# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.

# You must implement a solution with O(1) time complexity for each function.
# Methods pop, top and getMin operations will always be called on non-empty stacks.


import unittest


class MinStack:

    def __init__(self):
        self._elements = []
        self._minimums = []

    def push(self, val: int) -> None:
        if not self._minimums or val <= self._minimums[-1]:
            self._minimums.append(val)
        self._elements.append(val)

    def pop(self) -> None:
        if self._elements[-1] == self._minimums[-1]:
            self._minimums.pop()
        self._elements.pop()

    def top(self) -> int:
        return self._elements[-1]

    def getMin(self) -> int:
        return self._minimums[-1]


class TestMinStack(unittest.TestCase):
    def test_minStack(self):
        stack = MinStack()

        stack.push(1)
        stack.push(2)
        stack.push(3)
        last_elem = stack.top()
        self.assertEqual(3, last_elem)

        stack.pop()
        last_elem = stack.top()
        self.assertEqual(2, last_elem)

        minimum = stack.getMin()
        self.assertEqual(1, minimum)

        stack.push(-1)
        stack.push(-1)
        stack.push(-1)
        stack.push(-1)
        minimum = stack.getMin()
        self.assertEqual(-1, minimum)

        stack.pop()
        stack.pop()
        stack.pop()
        minimum = stack.getMin()
        self.assertEqual(-1, minimum)

        stack.pop()
        minimum = stack.getMin()
        self.assertEqual(1, minimum)

