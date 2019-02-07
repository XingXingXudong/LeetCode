# coding: utf-8

from array2tree import Tree
from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        cur = root
        next_ = cur.left

        while next_:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next_
                next_ = cur.left

    def connect_1(self, root):
        if not root:
            return
        queue = deque()
        queue.append((0, root))
        old_level = 0
        work_queue = list()
        while queue:
            level, node = queue.popleft()
            if work_queue and level > old_level:
                for i in range(len(work_queue)-1):
                    work_queue[i].next = work_queue[i+1]
                    work_queue.clear()
            work_queue.append(node)
            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))
                

if __name__ == '__main__':
    array = list(range(1, 4))
    print(array)
    tree = Tree()
    root = tree.array2tree(array)
    print(root)
    Solution().connect_1(root)
    

