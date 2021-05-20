#!/usr/bin/python3
"""[MRUCache]
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """[MRUCache]

    Args:
        BaseCaching ([class]): [BaseCaching module]
    """
    def __init__(self):
        """[initialization]
        """
        super().__init__()
        self.current_cache = []

    def put(self, key, item):
        """[put]

        Args:
            key ([str]): [key]
            item ([str]): [value to assign]
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.current_cache:
                self.current_cache.append(key)
            else:
                self.current_cache.append(
                    self.current_cache.pop(self.current_cache.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.current_cache.pop(-2)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """[get by key]

        Args:
            key ([str]): [key]

        Returns:
            [type]: [return value or none]
        """
        if key and key in self.cache_data:
            self.current_cache.append(
                self.current_cache.pop(self.current_cache.index(key)))
            return self.cache_data.get(key)
        return None
