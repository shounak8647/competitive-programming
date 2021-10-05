class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printLevelOrder(node):
    h = height(node)
    for i in range(1, h+1):
        printCurrentLevel(node, i)


def printCurrentLevel(node, level):
    if node is None:
        return
    if level == 1:
        print(node.data)
    if level > 1:
        printCurrentLevel(node.left, level-1)
        printCurrentLevel(node.right, level-1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        return max(lheight, rheight)+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)
