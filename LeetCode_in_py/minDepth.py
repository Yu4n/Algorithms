from definition import TreeNode


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            k = len(queue)
            for _ in range(k):
                node = queue[0]
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queue.pop(0)
