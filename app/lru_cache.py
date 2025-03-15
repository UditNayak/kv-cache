from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str):
        if key not in self.cache:
            return None
        # Move accessed item to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: str, value: str):
        if key in self.cache:
            # Update value and move to end
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Evict the least recently used item
            self.cache.popitem(last=False)
        self.cache[key] = value