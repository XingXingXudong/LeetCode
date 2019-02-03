# coding: utf-8


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or root.left == root.right:
            return True
        left_sub_tree = []
        right_sub_tree = []
        def helper_left(node):
            if not node:
                return
            helper_left(node.left)
            left_sub_tree.append(node.val)
            helper_left(node.right)
        helper_left(root.left)

        def helper_right(node):
            if not node:
                return
            helper_right(node.right)
            right_sub_tree.append(node.val)
            helper_right(node.left)
        helper_right(root.right)

        print(left_sub_tree)
        print(right_sub_tree)
        return left_sub_tree == right_sub_tree


if __name__ == '__main__':
    from array2tree import Tree
    tree = Tree()
    solution = Solution()

    # root_1 = tree.array2tree([1, 2, 2, 3, 4, 4, 3])
    # print(root_1)
    # print(solution.isSymmetric(root_1))
    # root_2 = tree.array2tree([1, 2, 2, None, 4, None, 3])
    # print(root_2)
    # print(solution.isSymmetric(root_1))
    root_3 = tree.array2tree([1,2,3,3,None,2,None])
    print(root_3)
    print(solution.isSymmetric(root_3))




