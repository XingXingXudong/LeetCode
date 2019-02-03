# coding: utf-8
from collections import deque

class Solution(object):
    def hasPathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return 0 == sum_
        queue = deque()
        queue.append((root, root.val))
        while queue:
            print(queue)
            r, s = queue.popleft()
            if r.left is None and r.right is None and s == sum_:
                return True
            if r.left is not None and sum_ >= s + r.left.val:
                queue.append((r.left, s + r.left.val))
            if r.right is not None and sum_ >= s + r.right.val:
                queue.append((r.right, s + r.right.val))
        return False


if __name__ == "__main__":
    from array2tree import Tree
    tree = Tree()
    root = tree.array2tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print(root)

    solution = Solution()
    print(solution.hasPathSum(root, 22))

