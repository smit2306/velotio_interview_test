import collections
import logging


class LruCache:

    # we can have our doubly linked list implementation and use that class below
    cacheClass = collections.OrderedDict

    def __init__(self, cache_size: int):
        self.cache = self.cacheClass()
        self.cache_size = cache_size
        self.logger = logging.getLogger(__name__)

    def get(self, key: int) -> int:

        if key not in self.cache.keys():
            self.logger.info(f"Key: {key} not in cache!")
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cache_size:
            self.logger.info("Cache overflow, deleting the least recently used cache")
            self.cache.popitem(last=False)
