#!/usr/bin/python3
"""[holb]
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """[BasicCache]

    Args:
        holb ([class]): [holb module]
    """
    def __init__(self):
    """[BasicCache]

    Args:
        holb ([class]): [holb module]
    """
        super().__init__()
        self.current_cache = []

    def put(self, key, item):
    """[BasicCache]

    Args:
        holb ([class]): [holb module]
    """
        if key and item:
            self.cache_data[key] = item
            if key not in self.current_cache:
                self.current_cache.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                dist = self.current_cache.pop(0)
                del self.cache_data[dist]
                print("DISCARD: {}".format(dist))

    def get(self, key):
    """[BasicCache]

    Args:
        holb ([class]): [holb module]
    """
        return self.cache_data.get(key) or None
