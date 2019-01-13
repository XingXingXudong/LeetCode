# coding: utf-8

def valid_parentheses(s):
    """
    :type s:  str
    :rtype: bool
    """
    pd = {'(': ')', '{': '}', '[': ']'}
    stack = []
    if len(s) % 2 != 0:
        return False
    for c in list(s):
        if not c:
            return False
        if c in pd:
            stack.append(c)
        else: 
            if not(stack and pd[stack.pop()] == c):
                return False
    return len(stack) == 0


if __name__ == '__main__':
    print(valid_parentheses('(('))
    print(valid_parentheses('(())'))
    print(valid_parentheses('([]())'))

