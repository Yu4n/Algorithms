from definition import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root


pre = [3, 9, 1, 2, 20, 15, 7]
IN = [1, 9, 2, 3, 15, 20, 7]
x = Solution()
rt = x.buildTree(pre, IN)
