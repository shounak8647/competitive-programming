class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def insertData(arr, root, i, n):

    if i < n:
        temp = Node(arr[i])
        root = temp

        root.left = insertData(arr, root.left, 2 * i + 1, n)

        root.right = insertData(arr, root.right, 2 * i + 2, n)

    return root


def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.data, end=' ')
        InOrder(root.right)


arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
n = len(arr)
root = None
root = insertData(arr, root, 0, n)
InOrder(root)
