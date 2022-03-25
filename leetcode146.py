import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.cache.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        elif self.cap == len(self.cache):
            self.cache.popitem(0)    
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
