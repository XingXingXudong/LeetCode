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
        stack.append(root)
        while stack:
            if stack[-1].left:
                stack.append(stack[-1].left)
            else:
                cur = stack.pop()
                while not cur.right and stack:
                    rtn.append(cur.val)
                    cur = stack.pop()
                rtn.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
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

    def postorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rtn = list()
        if not root:
            return rtn
        stack = list()
        stack.append(root)
        while stack:
            cur = stack.pop()
            rtn.append(cur.val)
            left, right = cur.left, cur.right
            if left:
                stack.append(left)
            if right:
                stack.append(right)
        return rtn[::-1]

    def postorder_traversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rtn = []
        if not root:
            return rtn
        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            rtn.append(node.val)
        helper(root)
        return rtn

    def level_order_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rtn = []
        if not root:
            return rtn
        queue = list()
        queue.append(root)
        while queue:
            cur_val = list()
            cur_level = queue.copy()
            queue.clear()
            for x in cur_level:
                cur_val.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            rtn.append(cur_val)
        return rtn

    def max_depth_top_down(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        # def helper(root, d):
        #     self.depth = max(self.depth, d+1)
        #     if root.left:
        #         helper(root.left, d+1)
        #     if root.right:
        #         helper(root.right, d+1)
        # helper(root, 0)
        def helper(root, d):
            if not root:
                return 
            if not (root.left or root.right):
                self.depth = max(self.depth, d)
            helper(root.left, d+1)
            helper(root.right, d+1)
        helper(root, 1)
        return self.depth

    def max_depth_bottom_up(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0
            left_depth = helper(node.left)
            right_depth = helper(node.right)
            return max(left_depth, right_depth) + 1
        return helper(root)



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
    print(solution.postorder_traversal_recursive(node_1))
    print(solution.postorder_traversal(node_1))
    print(solution.level_order_traversal(node_1))
    print(solution.max_depth_top_down(node_1))
    print(solution.max_depth_bottom_up(node_1))

    only_node = TreeNode(1)
    print(solution.preorder_traversal(only_node))
    print(solution.preorder_traversal_recursive(only_node))
    print(solution.inorder_traversal(only_node))
    print(solution.inorder_traversal_recursive(only_node))
    print(solution.postorder_traversal(only_node))
    print(solution.level_order_traversal(only_node))
    print(solution.max_depth_top_down(only_node))
    print(solution.max_depth_bottom_up(only_node))

    node_a = TreeNode(1)
    node_b = TreeNode(3)
    node_b.left = node_a
    node_c = TreeNode(2)
    node_c.left = node_b

    print(solution.inorder_traversal(node_c))
    print(solution.inorder_traversal_recursive(node_c))
    print(solution.postorder_traversal_recursive(node_c))
    print(solution.postorder_traversal(node_c))
    print(solution.level_order_traversal(node_c))
    print(solution.max_depth_top_down(node_c))
    print(solution.max_depth_bottom_up(node_c))


