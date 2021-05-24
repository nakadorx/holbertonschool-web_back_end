#!/usr/bin/env python3
"""holb
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """holb
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """holb
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: callable):
    """holb
    """
    key = method.__qualname__
    inputs = "".join([key, ":inputs"])
    outputs = "".join([key, ":outputs"])
    inputs_list = method.self._redis.lrange(inputs, 0, -1)
    outputs_list = mehtod.self._redis.lrange(outputs, 0, -1)


def call_history(method: Callable) -> Callable:
    """holb
    """
    key = method.__qualname__
    inputs = "".join([key, ":inputs"])
    outputs = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """holb
        """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


class Cache:
    """holb
    """
    def __init__(self):
        """holb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """holb
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """holb
        """
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, data: bytes) -> str:
        """holb
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """holb
        """
        return int.from_bytes(data, sys.byteorder)
