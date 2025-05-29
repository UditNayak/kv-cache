from collections import OrderedDict
import psutil

class LRUCache:
    def __init__(self, memory_limit: float = 0.7):
        self.cache = OrderedDict()
        self.memory_limit = memory_limit  # 70% of total memory
    
    def get(self, key: str):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key) # Move accessed item to end (most recently used)
        return self.cache[key]

    def put(self, key: str, value: str):
        self.cache[key] = value  # Assign/update value
        self.cache.move_to_end(key)  # Move to end as most recently used
        self._evict_if_needed()

    def _evict_if_needed(self):
        while self._is_memory_exceeded():
            if self.cache:
                self.cache.popitem(last=False)  # Evict the least recently used item
            else:
                break

    def _is_memory_exceeded(self):
        memory_info = psutil.virtual_memory()
        return memory_info.percent / 100 > self.memory_limit