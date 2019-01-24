# coding: utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<val={}>".format(self.val)

    __str__ = __repr__


class Solution:

    def preorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = list()
        rtn = list()
        stack.append(root)
        while stack:
            cur = stack.pop()
            rtn.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return rtn

    def preorder_traversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rtn = list()
        def helper(node):
            rtn.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(root) 
        return rtn

    def inorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rtn = list()
        stack = list()
        traversed = set()
        stack.append(root)
        traversed.add(root)
        traversed.add(None)
        while stack:
            print(stack)
            print(rtn)
            print(traversed)
            if stack[-1].left and stack[-1].left not in traversed:
                stack.append(stack[-1].left)
                traversed.add(stack[-1].left)
            else:
                cur = stack.pop()
                rtn.append(cur.val)
                if cur.right and cur.right not in traversed:
                    stack.append(cur.right)
                    traversed.add(cur.right)
        return rtn

    def inorder_traversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        rtn = []
        
        # Note: 
        # helper_1和helper_2的逻辑本质上是一样的, 递归的处理left, root, right，区别在于
        # 判定有效节点的位置，helper_1在每次进入helper_1后判断，导致无效None节点
        # 多调用一次helper_1，使得其解的时间效率降低，而helper_2则在调用helper_2之前
        # 判断，通过预判减少了无效递归的次数，从而提高了效率。
        def helper_1(node):
            if node:
                helper_1(node.left)
                rtn.append(node.val)
                helper_1(node.right)

        def helper_2(node):
            if node.left:
                helper_2(node.left)
            rtn.append(node.val)
            if node.right:
                helper_2(node.right)

        # helper_1(root)   # 低效
        helper_2(root)    # 高效
        return rtn


if __name__ == '__main__':
    node_3 = TreeNode(3)
    node_2 = TreeNode(2)
    node_2.left = node_3
    node_1 = TreeNode(1)
    node_1.right = node_2
    print(node_1)
    solution = Solution()
    print(solution.preorder_traversal(node_1))
    print(solution.preorder_traversal_recursive(node_1))
    print(solution.inorder_traversal(node_1))
    print(solution.inorder_traversal_recursive(node_1))


