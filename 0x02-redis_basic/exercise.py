#!/usr/bin/env python3

""" Task1 exercise """

import redis, uuid
from typing import Union, Callable, Optional


class Cache:
    """declares a Cache redis class"""

    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        rand_num = str(uuid.uuid4())
        self._redis.set(rand_num, data)
        return rand_num

    def get(
        self, key: str, fn: Optional[callable] = None
    ) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """return value as a string"""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """return value as a intger"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
