from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.CAPACITY = capacity
        self.LRU = deque()
        self.kv = {}

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self.updateLRU(key)
        return self.kv[key]
        
    def put(self, key: int, value: int) -> None:
        if len(self.kv) == self.CAPACITY and key not in self.kv:
            self.evict()
        self.updateLRU(key)
        self.kv[key] = value

    def updateLRU(self, key: int) -> None:
        if key in self.kv:
            self.LRU.remove(key)
        self.LRU.appendleft(key)

    def evict(self) -> None:
        lastKey = self.LRU[-1]
        del self.kv[lastKey]
        self.LRU.pop()
