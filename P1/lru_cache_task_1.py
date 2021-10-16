class DoubleNode:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, node):
        if node is self.head:
            return
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        node.next = self.head
        self.head.previous = node
        node.previous = None
        self.head = node
        self.size += 1

    def delete(self, node):
        if self.head is None or node is None:
            return

        if self.tail == node:
            self.tail = node.previous
            node.previous.next = None
            self.size -= 1
            return

        if self.head == node:
            self.head = node.next
            node.next.previous = None
            self.size -= 1
            return

        node.previous.next = node.next
        node.next.previous = node.previous
        self.size -= 1

    def length(self):
        return self.size
    
    def remove_tail(self):
        self.tail.previous.next = None
        self.tail = self.tail.previous

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.valueDict = {}
        self.doublyLinkedList = DoublyLinkedList()
        self.node = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.valueDict.keys():
            node = self.valueDict[key]
            self.doublyLinkedList.delete(node)
            self.doublyLinkedList.prepend(node)
            return print(node.value)
        else:
            return print(-1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        node = DoubleNode(value, key)
        self.valueDict[key] = node
        if self.doublyLinkedList.length() == self.capacity:
            del self.valueDict[self.doublyLinkedList.tail.key]
            self.doublyLinkedList.remove_tail()
            self.doublyLinkedList.prepend(node)
        else:
            self.doublyLinkedList.prepend(node)

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

