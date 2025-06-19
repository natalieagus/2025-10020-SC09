class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# sum all node values
def tree_sum(node):
    if not node:
        return 0
    return node.val + tree_sum(node.left) + tree_sum(node.right)

# count number of nodes
def tree_count(node):
    if not node:
        return 0
    return 1 + tree_count(node.left) + tree_count(node.right)

# composed: use both tree_count and tree_sum
def tree_average(node):
    count = tree_count(node)
    return tree_sum(node) / count if count != 0 else 0

if __name__ == "__main__":
    root = Node(5,
                Node(3, Node(1), Node(4)),
                Node(8, None, Node(10)))

    print("Sum:", tree_sum(root))         
    print("Count:", tree_count(root))     
    print("Average:", tree_average(root)) 
