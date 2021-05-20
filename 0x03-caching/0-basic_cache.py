#!/usr/bin/python3
"""[holberton]
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """[BasicCache]

    Args:
        holb ([class]): [holb module]
    """
    def put(self, key, item):
    """[BasicCache]

    Args:
        holb ([class]): [holb module]
    """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
    """[BasicCache]

    Args:
        holb ([class]): [holb module]
    """
        return self.cache_data.get(key) or None
