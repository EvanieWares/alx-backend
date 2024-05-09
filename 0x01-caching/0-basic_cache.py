#!/usr/bin/env python3
"""
Basic ditionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    a class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """
        Adds an item to the cache dictionary with the given key.

        Parameters:
            key (Any): The key to associate the item with.
            item (Any): The item to be added to the cache.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get the value associated with the given key from the cache_data
        dictionary.

        Parameters:
            key (Any): The key to search for in the cache_data dictionary.

        Returns:
            Any: The value associated with the given key in the cache_data
            dictionary, or None if the key is not found.
        """
        return self.cache_data.get(key, None)
