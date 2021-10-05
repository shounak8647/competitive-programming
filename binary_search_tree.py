class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# def insert(root, key):
#     newNode = Node(key)
#     if root == None:
#         return newNode
#     else:
#         if root.data == key:
#             return root
#         elif key > root.data:
#             if root.right is None:
#                 root.right = newNode
#             else:
#                 insert(root.right, key)
#         else:
#             if root.left is None:
#                 root.left = newNode
#             else:
#                 insert(root.left, key)
#     print('Current Node:', root.data)

def insert(root, key):
    newNode = Node(key)
    if root is None:
        return newNode
    else:
        if root.data == key:
            return root
        if key > root.data:
            if root.right is None:
                root.right = newNode
            else:
                insert(root.right, key)
        elif key < root.data:
            if root.left is None:
                root.left = newNode
            else:
                insert(root.left, key)


def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data)
        InOrder(root.right)


def levelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        currentLevel(root, i)


def currentLevel(root, level):
    if root is None:
        return
    else:
        if level == 1:
            print(root.data)
        elif level > 1:
            currentLevel(root.left, level-1)
            currentLevel(root.right, level-1)


def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        return max(lheight, rheight)+1


def bfsQue(root):
    if root is None:
        return

    que = [root]

    while len(que) > 0:
        print(que[0].data)
        node = que.pop(0)

        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)


r = Node(50)
insert(r, 30)
insert(r, 20)
insert(r, 40)
insert(r, 70)
insert(r, 60)
insert(r, 80)

# InOrder(r)
# levelOrder(r)
bfsQue(r)
