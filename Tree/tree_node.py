# coding: utf-8
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        val = str(self.val)
        if self.next is None:
            val += '#'
        ch = []
        queue = deque()
        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)
        while queue:
            cur = queue.popleft()
            ch.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        ch_str = ""
        if ch:
            ch_str = "<" + ",".join(str(x) for x in ch) + ">"

        return val + '-' + ch_str

    __str__ = __repr__

