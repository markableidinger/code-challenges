'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

def valid_parentheses(s):
    matching = {
    '{' : '}',
    '[' : ']',
    '(' : ')'
    }
    open_stack = []
    for char in s:
        if matching.get(char, None) is not None:
            open_stack.append(char)
        else:
            if len(open_stack) == 0:
                return False
            if matching[open_stack[-1]] == char:
                open_stack.pop()
            else:
                return False
    return len(open_stack) == 0

