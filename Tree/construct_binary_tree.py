# coding: utf-8

from tree_node import TreeNode

class Solution:
    def build_tree_from_in_post(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        print("inorder: ", inorder)
        print("postorder: ", postorder)
        print("==============================")
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inorder_index = inorder.index(root.val)

        root.right = self.build_tree_from_in_post(inorder[inorder_index+1:], postorder)
        root.left = self.build_tree_from_in_post(inorder[:inorder_index], postorder)

        return root

    def build_tree_from_in_post_0(self, inoder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        map_inorder = {val: i for i, val in enumerate(inoder)}
        def recur(low, high):
            print("low = {}, high = {}".format(low, high))
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inoder)-1)

    def build_tree_from_pre_inorder(self, preorder, inorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        print("preorder: ", preoder)
        print("inorder: ", inorder)
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        ind = inorder.index(root.val)
        root.left = self.build_tree_from_pre_inorder(preorder, inorder[:ind])
        root.right = self.build_tree_from_pre_inorder(preorder, inorder[ind+1:])
        return root


if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    # postorder = [9,15,7,20,3]
    preoder = [3, 9, 20, 15, 7]
    solution = Solution()
    # print(solution.build_tree_from_in_post(inorder, postorder))
    # print(solution.build_tree_from_in_post_0(inorder, postorder))
    print(solution.build_tree_from_pre_inorder(preoder, inorder))

