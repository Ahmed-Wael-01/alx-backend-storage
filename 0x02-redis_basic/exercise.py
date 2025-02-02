#!/usr/bin/env python3
"""cache class with redis"""
import redis, uuid
from typing import Union, Optional, Callable


class Cache:
    """cache class that uses redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key):
        return str(self._redis.get(key))

    def get_int(self, key):
        value = self._redis.get(key)
        try:
            value = int(value)
        except Exception:
            value = 0
        return value
