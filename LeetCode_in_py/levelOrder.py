from definition import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level = []
            k = len(queue)
            for i in range(k):
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                level.append(queue.pop(0).val)
            res.append(level)
        return res
