# coding: utf-8

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for s in tokens:
        if '+' == s:
            r = stack.pop()
            l = stack.pop()
            stack.append(l + r)
        elif '-' == s:
            r = stack.pop()
            l = stack.pop()
            stack.append(l - r)
        elif '*' == s:
            r = stack.pop()
            l = stack.pop()
            stack.append((l) * (r))
        elif '/' == s:
            r = stack.pop()
            l = stack.pop()
            # Division between two integers should truncate toward zero.
            stack.append(int(float(l)/ (r)))
        else:
            stack.append(int(s))
        print(stack)
    return stack.pop()
        

if __name__ == '__main__':
    a = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert evalRPN(a) == 22



