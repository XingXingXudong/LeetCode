# coding: utf-8

"""
Construct a binary tree from array
    array: [[1, 2, 3, null, 3, null, 3]
    tree:
         1
       /   \
      2     2
       \     \
        3     3 
"""

from collections import deque
from tree_node import TreeNode

class Tree:
    def array2tree(self, array):
        self.root = None
        if not array:
            return
        queue = deque()
        self.root = TreeNode(array[0])
        queue.append(self.root)

        array_queue = deque(array[1:])
        while array_queue:
            l = array_queue.popleft()
            r = array_queue.popleft()
            cur_node = queue.popleft()
            if l:
                cur_node.left = TreeNode(l)
                queue.append(cur_node.left)
            if r:
                cur_node.right = TreeNode(r)
                queue.append(cur_node.right)
        return self.root

if __name__ == '__main__':
    # array = [3, 9, 20, None, None, 15, 7]
    array = [1, 2, 2, 3, 4, 4, 3]
    tree = Tree()
    root = tree.array2tree(array)
    print(root)

