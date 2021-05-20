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
        """[get]

        Args:
            key ([str]): [key to the dict]

        Returns:
            [str / None]: [get value by key]
        """
        return self.cache_data.get(key) or None
