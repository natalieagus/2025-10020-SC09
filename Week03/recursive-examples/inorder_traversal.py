class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print("inorder_traversal(TreeNode):", inorder_traversal(root))


# Iterative version using a stack
def inorder_traversal_iterative(root):
    result, stack = [], []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

if __name__ == "__main__":
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print("inorder_traversal_iterative(TreeNode):", inorder_traversal_iterative(root))
