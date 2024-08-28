#!/usr/bin/env python3

""" Task1 exercise """

import redis, uuid
from typing import Union


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
