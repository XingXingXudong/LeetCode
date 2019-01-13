# coding: utf-8

from collections import deque
import math

def perfect_square(n):
    if n < 4:
        return n
    qeuen = deque([(n, 0)])
    while qeuen:
        cur, step = qeuen.popleft()
        if cur == 0:
            return step
        for i in range(int(math.sqrt(cur)) + 1):
            remain = cur - i*i
            if 0 == remain:
                return step + 1
            else:
                qeuen.append((remain, step + 1))


if __name__ == '__main__':
    for i in range(500, 2000):
        print(i, perfect_square(i))

