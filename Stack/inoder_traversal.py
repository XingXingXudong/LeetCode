# coding: utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        # return "<val={}, left={}, right={}>".format(self.val, self.left, self.right)
        return "<val={}>".format(self.val)

    __str__ = __repr__


class Solution(object):
    def inorder_traversal(self, root):
        """
        type root: TreeNode
        rtype: List[int]
        """
        if not root:
            return

        stack = list()
        traversed = set()
        rtn = []
        stack.append(root)
        while stack:
            print("rtn: ", rtn)
            print("stack: ", stack)
            cur = stack[-1]
            if cur.left and cur.left not in traversed:
                stack.append(cur.left)
                traversed.add(cur.left)
            else:
                rtn.append(stack.pop())
                if cur.right:
                    stack.append(cur.right)
        return rtn

    def inorder_traversal_recursive(self, root):
        rtn = []
        def helper(root, rtn):
            if not root:
                return
            helper(root.left, rtn)
            rtn.append(root)
            helper(root.right, rtn)
        helper(root, rtn)
        return rtn


if __name__ == '__main__':
    node_3 = TreeNode(3)
    node_2 = TreeNode(2)
    node_2.left = node_3
    node_1 = TreeNode(1)
    node_1.right = node_2
    print(node_1)
    solution = Solution()
    print(solution.inorder_traversal(node_1))
    print(solution.inorder_traversal_recursive(node_1))



