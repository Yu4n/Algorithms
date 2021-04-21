from definition import TreeNode


# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why
class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        inorderIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorderIndex + 1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root

    def buildTree_(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        def recur(low, high):
            if low > high:
                return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid + 1, high)
            x.left = recur(low, mid - 1)
            return x

        return recur(0, len(inorder) - 1)
