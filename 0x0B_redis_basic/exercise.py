#!/usr/bin/env python3
"""[summary]
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """[count how many times methods
        of the Cache class are called]

    Args:
        method (Callable): [the method to count]

    Returns:
        Callable: [returned callable]
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """[wrapper]
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: callable):
    """[replay]
    """
    key = method.__qualname__
    inputs = "".join([key, ":inputs"])
    outputs = "".join([key, ":outputs"])
    inputs_list = method.self._redis.lrange(inputs, 0, -1)
    outputs_list = mehtod.self._redis.lrange(outputs, 0, -1)


def call_history(method: Callable) -> Callable:
    """[call_history]

    Args:
        method (Callable): [method to store
        the history of inputs and outputs ]

    Returns:
        Callable: [callable]
    """
    key = method.__qualname__
    inputs = "".join([key, ":inputs"])
    outputs = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """[wrapper]
        """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


class Cache:
    """[Cache]
    """
    def __init__(self):
        """[__init__]
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """[store]

        Args:
            data (Union[str, bytes, int, float]): [data]

        Returns:
            str: [returns a generated random key]
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """[convert the data back to the desired format]

        Args:
            key (str): [key]
            fn (Optional[Callable], optional): [Callable]. Defaults to None.

        Returns:
            Union[str, bytes, int, float]: [data returned]
        """
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, data: bytes) -> str:
        """[get_str]

        Args:
            data (bytes): [data to convert to str]

        Returns:
            str: [converted data]
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """[get_int]

        Args:
            data (bytes): [data to be converted to int]

        Returns:
            int: [converted data]
        """
        return int.from_bytes(data, sys.byteorder)