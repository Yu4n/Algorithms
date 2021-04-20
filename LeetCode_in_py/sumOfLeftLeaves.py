from definition import TreeNode


class Solution:
    def __init__(self):
        self.sum_ = 0

    def dfs(self, root):
        if root:
            if root.left and not root.left.left and not root.left.right:
                self.sum_ += root.left.val
            self.dfs(root.left)
            self.dfs(root.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.sum_
