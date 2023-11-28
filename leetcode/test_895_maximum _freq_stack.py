# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
#
# Implement the FreqStack class:
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


import unittest


class FreqStack:
    def __init__(self):
        self.max_freq = 0  # max frequency of all elements
        self.element_freqs = {}  # frequency of each element (key - element, val - frequency)
        self.freqs = {}  # key - frequency, vel - stack of corresponding elements

    def push(self, val: int) -> None:
        if val not in self.element_freqs:
            self.element_freqs[val] = 0
        self.element_freqs[val] += 1

        self.max_freq = max(self.max_freq, self.element_freqs[val])

        if self.element_freqs[val] not in self.freqs:
            self.freqs[self.element_freqs[val]] = []
        self.freqs[self.element_freqs[val]].append(val)

    def pop(self) -> int:
        result = self.freqs[self.max_freq].pop()
        self.element_freqs[result] -= 1
        if not self.freqs[self.max_freq]:
            self.max_freq -= 1
        return result


class TestFreqStack(unittest.TestCase):
    def test_freqStack(self):
        stack = FreqStack()
        stack.push(5)
        self.assertEqual(1, stack.max_freq)
        self.assertEqual(1, len(stack.element_freqs))
        self.assertEqual(1, stack.element_freqs[5])
        stack.push(7)
        stack.push(5)
        stack.push(7)
        stack.push(4)
        stack.push(5)
        self.assertEqual(3, stack.max_freq)
        self.assertEqual(3, len(stack.element_freqs))
        self.assertEqual(3, stack.element_freqs[5])

        self.assertEqual(5, stack.pop())
        self.assertEqual(7, stack.pop())
        self.assertEqual(5, stack.pop())
        self.assertEqual(4, stack.pop())
