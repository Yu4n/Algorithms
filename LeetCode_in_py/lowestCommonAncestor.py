class Solution:
    def lowestCommonAncestor(self, root, p, q):
        return root if (root.val - p.val) * (root.val - q.val) < 1 else self.lowestCommonAncestor(
            (root.left, root.right)[p.val > root.val], p, q)
