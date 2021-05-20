#!/usr/bin/python3
"""[FIFOCache]
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """[BasicCache]

    Args:
        holb ([class]): [holb module]
    """
    def __init__(self):
        """[inti]
        """
        super().__init__()
        self.current_cache = []

    def put(self, key, item):
        """[holb]

        Args:
            key ([str]): [kk]
            item ([str]): [value to assign]
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.current_cache:
                self.current_cache.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.current_cache.pop(0)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """[get by key]

        Args:
            key ([s]): [key]

        Returns:
            [t]: [0]
        """
        return self.cache_data.get(key) or None