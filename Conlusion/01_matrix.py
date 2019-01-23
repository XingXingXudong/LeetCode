# coding: utf-8

import collections
from pprint import pprint

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        rtn = [1000000] * cols
        rtn = [rtn.copy() for i in range(rows)]

        queue = collections.deque()
        traversed = set()

        for r, row in enumerate(matrix):
            for l, cur in enumerate(row):
                if cur == 0:
                    queue.append((r, l, 0))
                    traversed.add((r, l))

        while queue:
            print(queue)
            r, l, val = queue.popleft()
            # print("[", r, ", ", l, '] = ', val)
            # rtn[r][l] = min(rtn[r][l], matrix[r][l], val)
            rtn[r][l] = min(rtn[r][l], val)
            pprint("matrix: \n")
            pprint(matrix)
            pprint("rtn: \n")
            pprint(rtn)
            if r-1 >= 0 and (r-1, l) not in traversed:
                queue.append((r-1, l, rtn[r][l]+1))
                traversed.add((r-1, l))
            if r+1 < rows and (r+1, l) not in traversed:
                queue.append((r+1, l, rtn[r][l]+1))
                traversed.add((r+1, l))
            if l-1 >= 0 and (r, l-1) not in traversed:
                queue.append((r, l-1, rtn[r][l]+1))
                traversed.add((r, l-1))
            if l+1 < cols and (r, l+1) not in traversed:
                queue.append((r, l+1, rtn[r][l]+1))
                traversed.add((r, l+1))
        
        return rtn


if __name__ == '__main__':
    # ipt = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # ipt = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    ipt = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
    opt = Solution().updateMatrix(ipt)
    print(opt)
