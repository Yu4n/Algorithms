from definition import TreeNode


# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why
class Solution:
    def buildTree_(self, inorder, postorder):
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex + 1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root

    def buildTree(self, inorder, postorder) -> TreeNode:
        def recur(root, left, right):
            if left > right:
                return  # 递归终止
            node = TreeNode(postorder[root])  # 建立根节点
            i = dic[postorder[root]]  # 划分根节点、左子树、右子树
            print("left: " + str(left) + ". right: " + str(right))
            node.right = recur(root - 1, i + 1, right)  # 开启右子树递归
            node.left = recur(root - 1 - right + i, left, i - 1)  # 开启左子树递归
            return node  # 回溯返回根节点

        dic, postorder = {}, postorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(len(inorder) - 1, 0, len(inorder) - 1)
