class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_binary_tree_recursive(tree):
    x = tree
    if x is not None:
        print_binary_tree_recursive(x.left)
        print(x.val)
        print_binary_tree_recursive(x.right)


def print_binary_tree_non_recursive(tree):
    ls = [tree]
    while len(ls) > 0:
        x = ls[len(ls) - 1]
        while x is not None:
            ls.append(x.left)
            x = ls[len(ls) - 1]
        ls.pop()
        if len(ls) > 0:
            x = ls.pop()
            print(x.val)
            ls.append(x.right)


def inorder_tree_walk(root):
    if root:
        inorder_tree_walk(root.left)
        print(root.val)
        inorder_tree_walk(root.right)


def inorder_non_recursive(root):
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            print(curr.val, end=' ')
            curr = curr.right
        else:
            break


def tree_minimum(root):
    while root.left:
        root = root.left
    return root.val


def tree_maximum(root):
    while root.right:
        root = root.right
    return root.val


def tree_insert(root, key):
    z = TreeNode(key)
    y = None
    x = root
    while x:
        y = x
        if z.val < x.val:
            x = x.left
        else:
            x = x.right
    if y is None:
        return z
    elif z.val < y.val:
        y.left = z
    else:
        y.right = z


def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if root == None:
        return root
    # Find node
    if key < root.val:  # if less
        root.left = deleteNode(root.left, key)
    elif key > root.val:  # if greater
        root.right = deleteNode(root.right, key)

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
            minRoot = findMinNode(root.right)
            root.val = minRoot.val
            root.right = deleteNode(root.right, root.val)

    return root


def findMinNode(self, root: TreeNode) -> TreeNode:
    current = root

    # loop down to find the lefmost leaf
    while (current.left is not None):
        current = current.left

    return current


if __name__ == '__main__':
    Root = None
    '''
    Root.left = TreeNode(2)
    Root.right = TreeNode(6)
    Root.left.left = TreeNode(1)
    Root.left.right = TreeNode(3)
    Root.right.left = TreeNode(5)
    Root.right.right = TreeNode(7)
    '''
    if Root is None:
        Root = tree_insert(Root, 8)
    else:
        tree_insert(Root, 8)
    tree_insert(Root, 7)
    tree_insert(Root, 6)
    Root = deleteNode(Root, 7)
    inorder_non_recursive(Root)
