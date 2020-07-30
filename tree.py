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


if __name__ == '__main__':
    Root = TreeNode(1)
    Root.left = TreeNode(2)
    Root.right = TreeNode(3)
    Root.left.left = TreeNode(4)
    Root.left.right = TreeNode(5)
    Root.right.left = TreeNode(6)
    Root.right.right = TreeNode(7)
    print_binary_tree_non_recursive(Root)
