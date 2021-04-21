# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
from definition import TreeNode

class Solution:
    def __init__(self):
        self.sum_ = 0
    def dfs(self, root):
        if root:
            if root.left:
                self.sum_ += root.left.val
            self.dfs(root.left)
            self.dfs(root.right)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        sum_ = 0
        self.dfs(root)
        return sum_
