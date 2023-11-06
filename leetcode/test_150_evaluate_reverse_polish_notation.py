# You are given an array of strings tokens that represents an arithmetic expression in a
# Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.


import unittest


def apply_operator(a: int, b: int, operator: str) -> int:
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return int(a / b)


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operands = []
        operators = {"+", "-", "/", "*"}

        for t in tokens:
            if t not in operators:
                operands.append(int(t))
            else:
                a = operands.pop()
                b = operands.pop()
                operands.append(apply_operator(b, a, t))

        return operands[0]


class TestSolutopn(unittest.TestCase):
    def test_evalRPN(self):
        solution = Solution()
        self.assertEqual(9, solution.evalRPN(["2", "1", "+", "3", "*"]))
        self.assertEqual(6, solution.evalRPN(["4", "13", "5", "/", "+"]))
        self.assertEqual(22, solution.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
