# coding: utf-8
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        values = [self.val]
        queue = deque()
        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)
        while queue:
            cur = queue.popleft()
            values.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        return ", ".join([str(x) for x in values])

    __str__ = __repr__

