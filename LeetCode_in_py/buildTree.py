from definition import TreeNode


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

    def buildTree_(self, preorder, inorder) -> TreeNode:
        def recur(root, left, right):
            if left > right:
                return  # 递归终止
            node = TreeNode(preorder[root])  # 建立根节点
            i = dic[preorder[root]]  # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)  # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right)  # 开启右子树递归
            return node  # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)


pre = [3, 9, 1, 2, 20, 15, 7]
IN = [1, 9, 2, 3, 15, 20, 7]
x = Solution()
rt = x.buildTree(pre, IN)
