# coding: utf-8

def daily_temp(T):
    """
    :type T: list
    :rtype : list
    """
    ans = [0] * len(T)
    stack = []
    for i, x in enumerate(T):
        while stack and T[stack[-1]] < x:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)
    return ans


if __name__ == '__main__':
   ta = [73,74,75,71,69,72,76,73]
   print(daily_temp(ta))

