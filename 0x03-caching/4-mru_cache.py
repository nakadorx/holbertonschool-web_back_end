#!/usr/bin/python3
"""[holb]
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
            else:
                self.current_cache.append(
                    self.current_cache.pop(self.current_cache.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.current_cache.pop(-2)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """[BasicCache]

        Args:
            holb ([class]): [holb module]
        """
        if key and key in self.cache_data:
            self.current_cache.append(
                self.current_cache.pop(self.current_cache.index(key)))
            return self.cache_data.get(key)
        return None
