class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail.next.previous = self.tail
        self.tail = node

    def prepend(self, node):
        if node is self.head:
            return
        node.next = self.head
        self.head.previous = node
        node.previous = None
        self.head = node

    def delete(self, node):
        if self.head is None or node is None:
            return

        if self.tail == node:
            self.tail = node.previous
            node.previous.next = None
            return

        if self.head == node:
            self.head = node.next
            node.next.previous = None
            return

        node.previous.next = node.next
        node.next.previous = node.previous


node_1 = DoubleNode(1, 1)
node_2 = DoubleNode(2, 2)
node_3 = DoubleNode(3, 3)
node_4 = DoubleNode(4, 4)
dll = DoublyLinkedList()
dll.append(node_1)
dll.append(node_2)
dll.append(node_3)
dll.append(node_4)
dll.delete(node_2)
print(dll.head.next.value)
