class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Dll:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print('Please enter a previous node.')
            return

        new_node = Node(new_data)
