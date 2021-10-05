class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


def PreOrder(root):
    if root:
        print(root.val)

        PreOrder(root.left)

        PreOrder(root.right)


def InOrder(root):
    if root:
        InOrder(root.left)

        print(root.val)

        InOrder(root.right)


def PostOrder(root):
    if root:
        PostOrder(root.left)

        PostOrder(root.right)

        print(root.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('PreOrder:')
PreOrder(root)
print('InOrder:')
InOrder(root)
print('PostOrder:')
PostOrder(root)
