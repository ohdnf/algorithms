class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

def search(value, node):
    if node is None or value == node.value:
        return node 
    elif value > node.value:
        return search(value, node.rightChild)
    elif value < node.value:
        return search(value, node.leftChild)

def insert(value, node):
    if value > node.value:
        pass


if __name__ == "__main__":
    node = TreeNode(1)
    node2 = TreeNode(10)
    root = TreeNode(50, node, node2)
    