class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.nodeLookup = {}

    # def __str__(self):
    #     debug = []
    #     current = self.sentinel.next
    #     while current != self.sentinel:
    #         debug.appe

    def popfront(self):
        node = self.sentinel.next
        assert node != self.sentinel
        self.sentinel.next = node.next
        node.next.prev = self.sentinel

        node.next = None
        node.prev = None

        del self.nodeLookup[node.val]
        return node.val

    def push(self, val):
        node = Node(val)
        self.nodeLookup[val] = node
        self.moveToBack(val)

    def moveToBack(self, val):
        assert val in self.nodeLookup
        node = self.nodeLookup[val]
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        self.sentinel.prev.next = node
        node.prev = self.sentinel.prev

        node.next = self.sentinel
        self.sentinel.prev = node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linkedlist = LinkedList()
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.linkedlist.moveToBack(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.linkedlist.moveToBack(key)
            return

        if len(self.cache) == self.capacity:
            delkey = self.linkedlist.popfront()
            del self.cache[delkey]

        self.linkedlist.push(key)
        self.cache[key] = value
