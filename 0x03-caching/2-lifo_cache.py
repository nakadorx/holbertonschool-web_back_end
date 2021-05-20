#!/usr/bin/python3
"""[holb]
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """[holb]

    Args:
        holb ([int]): [holb]
    """
    def __init__(self):
        """[initialization]
        """
        super().__init__()
        self.current_cache = []

    def put(self, key, item):
        """[holb]

        Args:
            holb ([int]): [holb]
            holb ([int]): [holb]
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.current_cache:
                self.current_cache.append(key)
            else:
                self.current_cache.append(next(reversed(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.current_cache.pop(-2)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """[holb]

        Args:
            holb ([int]): [holb]

        Returns:
            holb ([int]): [holb]
        """
        return self.cache_data.get(key) or None