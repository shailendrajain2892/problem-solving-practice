from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        value = -1
        if key in self.cache:
            value = self.cache.get(key)
            self.cache.move_to_end(key)
        return value
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

lRUCache =  LRUCache(2);
print(lRUCache.put(1, 10)) # cache: {1=10}
print(lRUCache.get(1))      # return -1 (not found)
print(lRUCache.get(1))   # return 10
print(lRUCache.put(2, 20))  # cache: {1=10, 2=20}
print(lRUCache.put(3, 30))  # cache: {2=20, 3=30}, key=1 was evicted
print(lRUCache.get(2))      # returns 20 



