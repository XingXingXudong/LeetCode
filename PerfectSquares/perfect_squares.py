# coding: utf-8
import math

def perfect_square(n):
    if n < 0:
        return 0
    res = [100] * (n + 1)
    res[0] = 0
    for i in range(1, len(res)):
        for j in range(1, int(math.sqrt(i))+1):
            if j*j <= i:
                res[i] = min(res[i], res[i - j*j] + 1)
    return res[-1]


if __name__ == '__main__':
    for i in range(1, 15):
        print(i, perfect_square(i))

