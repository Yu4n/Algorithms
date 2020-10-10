# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root
        # Find node
        if key < root.val:  # if less
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:  # if greater
            root.right = self.deleteNode(root.right, key)

        else:  # Node to delete
            # Case 1: No childs.
            if root.left == None and root.right == None:
                root = None

            # Case 2: One child
            elif root.left == None and root.right != None:
                root = root.right
            elif root.right == None and root.left != None:
                root = root.left

            # Case 3: 2 children
            else:
                minRoot = self.findMinNode(root.right)
                root.val = minRoot.val
                root.right = self.deleteNode(root.right, root.val)

        return root

    def findMinNode(self, root: TreeNode) -> TreeNode:
        current = root

        # loop down to find the lefmost leaf
        while (current.left is not None):
            current = current.left

        return current