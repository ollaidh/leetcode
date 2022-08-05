# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        paranth = {')': '(', ']': '[', '}': '{'}
        line_stack = []

        for par in s:
            if par in paranth:
                if line_stack and line_stack[-1] == paranth[par]:
                    line_stack.pop()
                else:
                    return False
            else:
                line_stack.append(par)
        if line_stack:
            return False
        return True


if __name__ == '__main__':
    line = Solution()

    if line.isValid('()') == True:
        print('()', 'Test OK')
    else:
        print('()', '- Test FAILED', '--- Expected: True, Got:', line.isValid('()'))

    if line.isValid('()[]{}') == True:
        print('()[]{}', 'Test OK')
    else:
        print('()[]{}', '- Test FAILED', '--- Expected: True, Got:', line.isValid('()[]{}'))

    if line.isValid('(]') == False:
        print('(]', 'Test OK')
    else:
        print('(]', '- Test FAILED', '--- Expected: False, Got:', line.isValid('(]'))