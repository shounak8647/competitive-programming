class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self, data):
        self.head = self.tail = Node(data)

    def enq(self, data):
        temp = Node(data)

        if self.tail == None:
            self.head = self.tail = temp
            return

        self.tail.next = temp
        self.tail = temp

    def dq(self):
        if self.head == None:
            return

        temp = self.head.next
        self.head = temp

        if self.head == None:
            self.tail = None

    def printq(self):
        temp = self.head
        result = []

        while temp:
            result.append(temp.data)
            temp = temp.next

        return result


myq = Queue(10)
myq.enq(20)
myq.enq(30)
myq.enq(40)
myq.dq()
myq.dq()
myq.dq()
print(myq.printq())
