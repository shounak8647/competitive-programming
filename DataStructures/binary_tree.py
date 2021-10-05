class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:

    def __init__(self):
        self.root = None

    def insertValue(self, data):

        currentNode = self.root

        if currentNode is None:
            self.root = Node(data)

        while currentNode:
            if data < currentNode.data:
                if currentNode.left is None:
                    currentNode.left = Node(data)
                    break
                currentNode = currentNode.left

            else:
                if currentNode.right is None:
                    currentNode.right = Node(data)
                    break
                currentNode = currentNode.right

    def printLeft(self):
        currentNode = self.root
        while currentNode:
            print("Left:", currentNode.data)
            currentNode = currentNode.left

    def printRight(self):
        currentNode = self.root
        while currentNode:
            print("Right:", currentNode.data)
            currentNode = currentNode.right


def PreOrder(root):
    if root:
        print(root.data)

        PreOrder(root.left)

        PreOrder(root.right)


def InOrder(root):
    if root:
        InOrder(root.left)

        print(root.data)

        InOrder(root.right)


def PostOrder(root):
    if root:
        PostOrder(root.left)

        PostOrder(root.right)

        print(root.data)


myTree = Tree()
myTree.insertValue(8)
myTree.insertValue(3)
myTree.insertValue(10)
myTree.insertValue(1)
myTree.insertValue(6)
myTree.insertValue(14)
myTree.insertValue(4)
myTree.insertValue(7)
myTree.insertValue(13)
# myTree.printLeft()
# myTree.printRight()
print('\nPreOrder:')
PreOrder(myTree.root)

print('\nInOrder:')
InOrder(myTree.root)

print('\nPostOrder:')
PostOrder(myTree.root)
