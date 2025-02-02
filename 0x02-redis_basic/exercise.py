#!/usr/bin/env python3
"""cache class with redis"""
import redis, uuid
from typing import Union


class Cache:
    """cache class that uses redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

