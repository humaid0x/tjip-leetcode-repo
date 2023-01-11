class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.CAPACITY = 2000
        self.data = [None] * self.CAPACITY

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        h = hash(key) % self.CAPACITY
        node = Node(key, value)
        node.next = self.data[h]
        self.data[h] = node

    def get(self, key: int) -> int:
        h = hash(key) % self.CAPACITY
        node = self.data[h]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        h = hash(key) % self.CAPACITY
        node = self.data[h]

        if node == None:
            return
        
        if node.key == key:
            self.data[h] = node.next
        else:
            while node and node.next:
                if node.next.key == key:
                    node.next = node.next.next
                node = node.next
                